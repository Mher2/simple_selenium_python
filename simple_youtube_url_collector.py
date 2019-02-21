from selenium.webdriver.common.action_chains import ActionChains
import constants as xpath
import methods as action

URL = "https://www.youtube.com/"
text_to_search = "films 2019"

action.driver.get(url=URL)
action.get_element_with_xpath(_xpath=xpath.search_input).send_keys(text_to_search)
action.get_element_with_xpath(_xpath=xpath.search_button).click()
action.get_element_with_xpath(_xpath=xpath.search_filters_button).click()

element = action.get_element_with_xpath(_xpath=xpath.search_filter_this_month)
ActionChains(action.driver).move_to_element(element).click().perform()

action.get_element_with_xpath(_xpath=xpath.search_hidden_filter_collapse)

all_videos_elements = action.get_all_elements_with_xpath(_xpath=xpath.video_title)

action.print_found_urls_hrefs(elements=all_videos_elements, count=10)

action.close_and_finish_execution()
