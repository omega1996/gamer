from selenium import webdriver, common
import time


class MyFarm:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open(self):
        self.driver.get("https://www.mojaderewnja.ru")
        # entry
        self.driver.find_element_by_name("username").send_keys("usr")
        self.driver.find_element_by_name("password").send_keys("pass")
        time.sleep(1)
        self.driver.find_element_by_id("loginbutton").click()
        time.sleep(10)
        # close
        try:
            self.driver.find_element_by_id("newsbox_close").click()
        except:
            pass

        try:
            self.driver.find_element_by_id("newsbox_close").click()
        except:
            pass

    def forward(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[7]/div[1]/div[1]/div[2]").click()
        time.sleep(3)

    def back(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[7]/div[1]/div[2]/div[2]").click()
        time.sleep(3)

    def farm(self, farm, place):
        time.sleep(0.5)
        self.driver.find_element_by_id("farm"+str(farm)+"_pos"+str(place)+"_click").click()
        time.sleep(0.5)
        print(place)
        try:
            self.driver.find_element_by_id("globalbox_button1").click()
        except:
            pass
        time.sleep(3)
        for i in range(10):
            try:
                self.driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[10]/div[10]/div[1]/div[1]/div"
                                                    ).click()  # покормить
            except:
                print('wtf error')
                pass
            time.sleep(0.5)
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[10]/div[22]"
                                          ).click()  # выход
        try:
            self.driver.find_element_by_xpath(
                "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[10]/div[22]").click()  # выход
        except:
            pass
        time.sleep(5)

    def seed(self, crop, fr, to):
        self.driver.find_element_by_id("rackitem"+str(crop)).click()  # зерно
        # всего ячеек 120
        for i in range(120)[fr:to:2]:
            try:
                self.driver.find_element_by_id("b"+str(i)).click()
            except:
                print("error")
                pass
            time.sleep(0.2)

    def plow(self):
        time.sleep(0.5)
        self.driver.find_element_by_id("farm1_pos1_click").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("cropall").click()
        time.sleep(0.5)
        try:
            self.driver.find_element_by_id("globalbox_button1").click()
        except common.exceptions.NoSuchElementException:
            pass
        time.sleep(0.5)
        self.seed(1, 1, 30)
        time.sleep(1)
        self.seed(3, 31, 60)
        time.sleep(1)
        self.seed(7, 61, 84)
        self.driver.find_element_by_id("rackswitch2").click()
        self.seed(108, 85, 120)
        self.driver.find_element_by_id("rackswitch1").click()
        self.seed(1, 109, 120)
        time.sleep(2)
        self.fill()
        self.driver.find_element_by_id("gardencancel").click()
        time.sleep(5)

    def fill(self):
        time.sleep(0.5)
        self.driver.find_element_by_id("giessen").click()
        time.sleep(0.5)
        for i in range(120)[::2]:
            try:
                self.driver.find_element_by_id("b"+str(i)).click()
                time.sleep(0.1)
            except:
                print("fill error")
                pass

    def cheese(self, farm, place):
        self.driver.find_element_by_id("farm" + str(farm) + "_pos" + str(place) + "_click").click()
        time.sleep(1)
        print(place)
        self.driver.find_element_by_id("production_slot"+str(farm)+"_"+str(place)+"_1").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_id("production_slot" + str(farm) + "_" + str(place)+"_1").click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(
                "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/div/div[49]\
                /div[1]/div/div/div/div[2]/div/div[2]/div[1]"
            ).click()
        except:
            pass
        try:
            self.driver.find_element_by_id("globalbox_button1").click()
        except:
            pass
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath(
                "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/\
                td[3]/div/div[49]/div[1]/div/div/div/div[2]/div/div[1]/div[1]"
            ).click()
        except common.exceptions.NoSuchElementException:
            try:
                self.driver.find_element_by_id("globalbox_button1").click()
            except:
                pass
            pass
        try:
            self.driver.find_element_by_id("globalbox_button1").click()
        except:
            pass
        time.sleep(3)
        try:
            self.driver.find_element_by_id("globalbox_close").click()
        except:
            pass
        time.sleep(3)
        self.driver.find_element_by_id("cancelscreen").click()  # выход

    def close(self):
        try:
            self.driver.find_element_by_id("logoutbutton").click()  # выход
        except:
            pass


start = MyFarm()
i = 0
while True:
    print('NUM: '+str(i))
    try:
        start.open()
        time.sleep(2)
        start.plow()
        start.farm(1, 2)  # eggs
        start.farm(1, 3)  # eggs
        start.farm(1, 4)  # cows
        start.cheese(1, 6)  # cheese
        start.forward()
        start.farm(2, 1)  # eggs
        start.farm(2, 3)  # bees
        start.farm(2, 5)  # goats
        start.cheese(2, 6)  # cheese
        start.close()
        time.sleep(1000)
    except:
        print("EPIC FAIL")
        continue
    i += 1

