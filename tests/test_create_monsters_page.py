import allure

from pages.create_monsters_page import CreateMonstersPage

class TestCreateMonstersPage:

    @allure.title("Create Monster")
    @allure.description("This test verifies if the monster is created")
    def test_create_monster(self, browser):
        monster_name = "test monster"
        self.create_monster_page = CreateMonstersPage(browser)
        self.create_monster_page.select_monster("monster-1")
        self.create_monster_page.set_name(monster_name)
        self.create_monster_page.set_hp(10)
        self.create_monster_page.set_attack(10)
        self.create_monster_page.set_defense(10)
        self.create_monster_page.set_speed(10)
        self.create_monster_page.click_on_create_monster()
        actual_result = self.create_monster_page.get_monsters_created()
        assert monster_name in actual_result, f"The {monster_name} is not created"
    
    @allure.title("Delete Monster")
    @allure.description("This test verifies if the monster is deleted")
    def test_delete_monster(self, browser):
        monster_name = "test monster"
        self.create_monster_page = CreateMonstersPage(browser)
        self.create_monster_page.select_monster("monster-1")
        self.create_monster_page.set_name(monster_name)
        self.create_monster_page.set_hp(10)
        self.create_monster_page.set_attack(10)
        self.create_monster_page.set_defense(10)
        self.create_monster_page.set_speed(10)
        self.create_monster_page.click_on_create_monster()
        self.create_monster_page.click_on_delete_monster(monster_name)
        actual_result = self.create_monster_page.get_monsters_created()
        assert monster_name not in actual_result, f"The {monster_name} is not deleted"
