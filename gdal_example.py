import gdal
from gdalconst import GDT_UInt16, GA_Update
import struct
import numpy


def create_if_not_exists(filename, etalon_raster, fill_value=0):
    raster = gdal.Open(filename, GA_Update)
    if raster is None:
        driver = etalon_raster.GetDriver()
        raster = driver.Create(
            filename,
            etalon_raster.RasterXSize,
            etalon_raster.RasterYSize,
            1,
            GDT_UInt16,
        )
        if raster is None:
            print("Failed to create raster " + filename)
            raise "Noise"
        raster.SetGeoTransform(etalon_raster.GetGeoTransform())
        raster.SetProjection(etalon_raster.GetProjection())

        raster.GetRasterBand(1).Fill(fill_value)

    return raster


def main():

    filename_1 = r"b01_tm_sin_i_2013_06_e.img"
    filename_2 = r"b02_tm_sin_i_2013_06_e.img"
    filename_sum = r"sum_test.img"

    raster_1 = gdal.Open(filename_1, gdal.GA_ReadOnly)
    raster_2 = gdal.Open(filename_2, gdal.GA_ReadOnly)

    band_1 = raster_1.GetRasterBand(1)
    band_2 = raster_2.GetRasterBand(1)

    raster_sum = create_if_not_exists(filename_sum, raster_1)

    band_out = raster_sum.GetRasterBand(1)

    size_x = raster_1.RasterXSize
    size_y = raster_1.RasterYSize

    for i_y in range(size_y):
        if i_y % 1000 == 0:
            print(i_y)

        scanline = band_1.ReadRaster(0, i_y, size_x, 1, size_x, 1, GDT_UInt16)
        val_1 = struct.unpack("H" * size_x, scanline)

        scanline = band_2.ReadRaster(0, i_y, size_x, 1, size_x, 1, GDT_UInt16)
        val_2 = struct.unpack("H" * size_x, scanline)

        vals_sum = [v1 + v2 for v1, v2 in zip(val_1, val_2)]
        vals_sum_out = numpy.asarray(
            [
                vals_sum,
            ],
            dtype=numpy.uint16,
        )

        band_out.WriteArray(vals_sum_out, 0, i_y)

    raster_1 = None
    raster_2 = None
    raster_sum = None


if __name__ == "__main__":
    main()
