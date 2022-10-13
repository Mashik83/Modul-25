import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_name_age_and_breed(go_to_my_pets):
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    pytest.driver.implicitly_wait(10)

    for i in range(len(pet_data)):
        pet_data_new = pet_data[i].text.replace('\n', '').replace('×', '')
        split_pet_data_new = pet_data_new.split(' ')
        result = len(split_pet_data_new)
        assert result == 3