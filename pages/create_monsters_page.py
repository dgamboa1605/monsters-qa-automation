from selenium.webdriver.common.by import By

class CreateMonstersPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.name_input = (By.CSS_SELECTOR, "[name='name']")
        self.hp_input = (By.CSS_SELECTOR, "[name='hp']")
        self.attack_input = (By.CSS_SELECTOR, "[name='attack']")
        self.defense_input = (By.CSS_SELECTOR, "[name='defense']")
        self.speed_input = (By.CSS_SELECTOR, "[name='speed']")
        self.craete_monster_button = (By.CSS_SELECTOR, "[data-testid='btn-create-monster']")
        self.monster_names = (By.CSS_SELECTOR, "[data-testid='card-monster-name']")

    def select_monster(self, monster_id):
        locator = f"[data-testid='{monster_id}']"
        self.driver.find_element(By.CSS_SELECTOR, locator).click()
    
    def set_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)
    
    def set_hp(self, hp):
        self.driver.find_element(*self.hp_input).send_keys(hp)
    
    def set_attack(self, attack):
        self.driver.find_element(*self.attack_input).send_keys(attack)
    
    def set_defense(self, defense):
        self.driver.find_element(*self.defense_input).send_keys(defense)
    
    def set_speed(self, speed):
        self.driver.find_element(*self.speed_input).send_keys(speed)

    def click_on_create_monster(self):
        self.driver.find_element(*self.craete_monster_button).click()
    
    def get_monsters_created(self):
        elements = self.driver.find_elements(*self.monster_names)
        names = [element.text for element in elements]
        return names

    def click_on_delete_monster(self, monster_name):
        locator = f"//p[contains(text(), '{monster_name}')]//parent::div//button[@data-testid='btn-delete']"
        self.driver.find_element(By.XPATH, locator).click()
