#encoding:utf-8
import xlwt


def createxls(result):
    """
    result: [{}, {}, {}...]
    """

    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
    # 表格标题
    title = ['a', 'b']

    #  添加列标题
    for i, t in enumerate(title):
        sheet.write(1, i, t)

    #  添加表格数据
    for i, row in enumerate(result):
        i += 2
        sheet.write(i, 0, row[''])
        sheet.write(i, 1, row[''])
        wbk.save('demo.xls')
