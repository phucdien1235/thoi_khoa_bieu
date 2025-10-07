from guizero import App, Text, Box
window = App(title = "Thời khóa biểu", width = 835, height = 155, layout = "grid")
for column in range(0,7):
    for row in range(0,6):
        if column < 2:
            box_content = Box(window, grid = [column, row], border = True)
            if row == 0 and column == 0:
                text_content = Text(box_content, text = "Buổi")
            elif row > 0 and column == 0:
                text_content = Text(box_content, text = "Sáng")
            elif row == 0 and column == 1:
                text_content = Text(box_content, text = "Tiết")
            elif row > 0 and column == 1:
                text_content = Text(box_content, text = str(row))
        if column >= 2:
            box_content = Box(window, grid = [column, row], border = True, width = 150, height = 26)
            if row > 0:
                if column == 2:
                    text_content = Text(window, grid = [2,1], text = "Chào cờ")
                    text_content = Text(window, grid = [2,2], text = "Ngữ văn")
                    text_content = Text(window, grid = [2,3], text = "Ngữ văn")
                    text_content = Text(window, grid = [2,4], text = "GDCD")
                    text_content = Text(window, grid = [2,5], text = "Địa lý")  
                elif column == 3:
                    text_content = Text(window, grid = [3,1], text = "Sinh học")
                    text_content = Text(window, grid = [3,2], text = "Tiếng Anh")
                    text_content = Text(window, grid = [3,3], text = "Công nghệ")
                    text_content = Text(window, grid = [3,4], text = "GDĐP")
                    text_content = Text(window, grid = [3,5], text = "Tin học")
                elif column == 4:
                    text_content = Text(window, grid = [4,1], text = "Lịch sử")
                    text_content = Text(window, grid = [4,2], text = "Toán")
                    text_content = Text(window, grid = [4,3], text = "Ngữ văn")
                    text_content = Text(window, grid = [4,4], text = "Tiếng Anh")
                    text_content = Text(window, grid = [4,5], text = "Sinh học")
                elif column == 5:
                    text_content = Text(window, grid = [5,1], text = "Hóa học")
                    text_content = Text(window, grid = [5,2], text = "Toán")
                    text_content = Text(window, grid = [5,3], text = "Tiếng Anh")
                    text_content = Text(window, grid = [5,4], text = "Địa lý")
                    text_content = Text(window, grid = [5,5], text = "Vật lý")
                elif column == 6:
                    text_content = Text(window, grid = [6,1], text = "Ngữ văn")
                    text_content = Text(window, grid = [6,2], text = "Toán")
                    text_content = Text(window, grid = [6,3], text = "Toán")
                    text_content = Text(window, grid = [6,4], text = "HĐTN")
                    text_content = Text(window, grid = [6,5], text = "SHL")
            elif row == 0:
                text_content = Text(box_content, text = "Thứ " + str(column))

window.display()