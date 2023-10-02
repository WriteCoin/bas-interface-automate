T = 10
PAUSE = 0.1

Settings.MoveMouseDelay = 0.05
Settings.DelayBeforeTyping = 0.01

img_folder = "images1366x768\\"

func_main_button = "ToFuncListButton.png"
add_function_button = "AddFunctionButtonBegin.png"
details_button = "DetailsButton.png"
new_name_func_pre = "NewNameFuncPre.png"
pencil = "Карандаш.png"

# проверка - вывод изображений
print(region_left_panel)
print(func_main_button)

class Region(Region):
    def image_wait(self, img, t = None):
        return image_wait(self, img, t)

    def image_find(self, img):
        return image_find(self, img)

#from org.sikuli.script import Match
#class Match(Match):
#    def __init__(self, m):
#        self.m = m
    
#    def image_wait(self, img, t = None):
#        return image_wait(self.m, img, t)

#    def image_find(self, img):
#        return image_find(self.m, img)

images = {}

def find_coords(images, reg, img):
    if reg in images:
        search_images = images[reg]
        if img in search_images:
            return search_images[img]
    images_nest = {k: v for k, v in images.items() if not isinstance(k, str)}
    res = None
    for v in images_nest.values():
        res = find_coords(v, reg, img)
    return res

def image_wait(reg, img, t = None):
    img = img_folder + img
    # print("Ожидание изображения")
    fnd = find_coords(images, reg, img)
    # print("Изображение:", fnd)
    if fnd is None:
        images[reg] = {}
        res = reg.wait(img, T and t is None or t)
        #def l_image_wait(img, t = None):
        #    return image_wait(res, img, t)
        #def l_image_find(img):
        #    return image_find(res, img)
        #setattr(res, 'image_wait', l_image_wait)
        #setattr(res, 'image_find', l_image_find)
        images[reg][img] = res
        return res
    return fnd

def image_find(reg, img):
    img = img_folder + img
    # print("Поиск изображения")
    fnd = find_coords(images, reg, img)
    # print("Изображение:", fnd)
    if fnd is None:
        images[reg] = {}
        res = reg.find(img)
        #def l_image_wait(img, t = None):
        #    return image_wait(res, img, t)
        #def l_image_find(img):
        #    return image_find(res, img)
        #setattr(res, 'fff', 1)
        #setattr(res, 'image_wait', l_image_wait)
        #setattr(res, 'image_find', l_image_find)
        images[reg][img] = res
        return res
    return fnd

#def obj_image_wait(self, img, t):
#    return image_wait(self, img, t)

#def obj_image_find(self, img):
#    return image_find(self, img)

#setattr(Region, 'image_wait', obj_image_wait)
#setattr(Region, 'image_find', obj_image_find)
#setattr(Match, 'image_wait', obj_image_wait)
#setattr(Match, 'image_find', obj_image_find)

#print("Match", Match)
#print(hasattr(Match, 'image_wait'))

region_left_panel = Region(0,76,505,462)
        
def wait_left_panel(img):
    # return region_left_panel.wait(img, T)
    #return region_left_panel.wait(img, T)
    return image_wait(region_left_panel, img, T)

def find_left_panel(img):
    # return region_left_panel.find(img)
    return image_find(region_left_panel, img)

def BAS_DisplayFuncList():
    print("Перейти в список функций")
    # region_left_panel.wait(func_main_button, T)
    # find_left_panel(func_main_button).click()
    region_left_panel.image_find(func_main_button).click()
    sleep(PAUSE)

def BAS_AddFunction(nameFunc, descFunc, isReturn, descReturn, nameReturnDefault, params):

    
    # region_left_panel.wait(add_function_button, T)
    #if not exists(add_function_button, T):
    #    print("Кнопка добавления не на экране")
    #    find_left_panel(func_main_button).click()
    # sleep(PAUSE)
    
    print("Добавление новой функции")
    region_left_panel.image_find(add_function_button).click()
    sleep(PAUSE)

    #if exists(details_button):
    #    click(details_button)
    #    sleep(PAUSE)

    #try:
    #    print("Включение подробного режима, если не включен")
    #    region_left_panel.wait(details_button, T)
    #    click(details_button)
    #except:
    #    pass

    #print("Тест вложенности")
    #Screen().wait("odno.png", T).wait("Browser.png", T).click()
    
    print("Изменение имени функции")
    m1 = region_left_panel.image_find(new_name_func_pre)
    image_find(m1, "pencil.png").click()
    sleep(PAUSE)
    
    # m1 = region_left_panel.wait(new_name_func_pre, T)
    # m1 = find_left_panel(new_name_func_pre)
    # image_find(m1, "pencil.png").click()
    # m1.find("pencil.png").click()
    # sleep(PAUSE)

    region_left_panel.image_find("AboutButton.png").click()
    # find_left_panel("AboutButton.png").click()
    sleep(PAUSE)
    region_left_panel.image_find(func_main_button).click()
    # find_left_panel(func_main_button).click()
    sleep(PAUSE)

    if params != 'a':
        BAS_DisplayFuncList()
        BAS_AddFunction(nameFunc, descFunc, isReturn, descReturn, nameReturnDefault, 'a')
    
    #m1 = region_left_panel.wait(new_name_func_pre, T)
    #print(m1)
    #m1.wait(pencil, T).click()

       
    # print("Кнопка для изменения имени новой функции")
    # region_left_panel.wait("Карандаш.png", T)
    # click("Карандаш.png")

    
    # "NewNameFuncPre.png".wait("Карандаш.png", T)
    # click("Карандаш.png")
    
    
        

def main():
    BAS_DisplayFuncList()
    BAS_AddFunction("Func1", "Описание функции", False, "", "", [])

main()