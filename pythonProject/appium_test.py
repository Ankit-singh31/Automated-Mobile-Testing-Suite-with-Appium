from asyncio import sleep
from turtledemo.penrose import start
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv.cli import unset
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random

def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "BQ99AIIVNNEQKJJV"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.rap.acadally"
    options.app_activity = "com.rap.acadally.MainActivity"
    options.no_reset = False
    options.auto_grant_permissions = True
    options.new_command_timeout = 300

    driver = webdriver.Remote("http://localhost:4724", options=options)
    driver.implicitly_wait(15)
    return driver

def handle_permission_dialog(driver):
    try:
        allow_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
        allow_button.click()
        print("Permission 'ALLOW' button clicked.")
    except Exception as e:
        print("No permission dialog found or error handling permissions. Continuing...")

def test_login():
    global child_elements
    driver = setup_driver()

    try:
        handle_permission_dialog(driver)
# username
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[1]"))
        )
        print("Username field found.")
        username_field.click()
        username_field.clear()
        username_field.send_keys("uat_107")
        print("Username entered.")

#forget password
        # forget_password = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Forgot Password"]'))
        # )
        # print("Forget password field found")
        # forget_password.click()
        #
        # username_field = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
        # )
        # username_field.click()
        # username_field.send_keys("uat_101")
        # print("Username entered")
        #
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageView[@content-desc='Submit & Next']"))
        # )
        # print("Submit/Next button found")
        # submit_button.click()
        # print("Submitted the 'Forgot Password' request")
        # try:
        #     otp_field = WebDriverWait(driver, 15).until(
        #         EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@content-desc='Enter OTP']"))
        #     )
        #     otp_field.click()
        #     print("OTP verification page loaded successfully.")
        # except Exception as e:
        #     print("OTP page did not load after clicking 'Submit & Next'.", e)
        #
        # otp_field = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText"))
        # )
        # otp_field.click()
        # print("Enter otp")
        #
        # submit_button = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Submit"]'))
        # )
        # submit_button.click()

#sign_in button
        sign_in_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Sign In"]'))
        )
        sign_in_button.click()
#password
        password_field = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[2]"))
        )
        print("Password field found.")
        password_field.click()
        password_field.send_keys("Ttaps@37")
        print("Password entered.")
#final sign_in
        sign_in_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Sign In"]'))
        )
        sign_in_button.click()
        print("Sign In button clicked to log in.")
        print("Login successful.")
#earn coins & gems
        try:
            # earn_coins=WebDriverWait(driver,20).until(
            #     EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Earn Coins"))
            # )
            # earn_coins.click()
            # print("10 Coins Collected")

            welcome_coin=WebDriverWait(driver,20).until(
                EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Claim"]'))
            )
            welcome_coin.click()
            print("Welcome coins and gems collected")

            try:
                check_coins_fallback = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]'))
                )
                check_coins_fallback.click()
                print("1st click for discovery coins after getting welcome coins.")

                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                                 '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]')))

                check_coins_fallback = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]'))
                )
                check_coins_fallback.click()
                print("2nd click for gems card after getting welcome gems.")

            except Exception as e:
                print(f"Fallback click on coins failed: {e}")
        except Exception as e:
            print("NO need to do any action.",e)

#Check coins
        check_coins=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc]'))
        )
        check_coins.click()
        print("Coins checked ")
        try:
            check_coins_fallback = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]'))
            )
            check_coins_fallback.click()
            print("1st click for discovery coins.")

            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]')))

            check_coins_fallback = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]'))
            )
            check_coins_fallback.click()
            print("2nd click for gems.")

        except Exception as e:
            print(f"Fallback click on coins failed: {e}")

#Gems

        # check_gems=WebDriverWait(driver,10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc]'))
        # )
        # check_gems.click()
        # print("Gems checked")
        #
        # increase_gems = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[6]'))
        # )
        # increase_gems.click()
        # print("Increased the number of gems to buy.")
        #
        # buy_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Buy"]'))
        # )
        # buy_button.click()
        # print("Gems purchased.")

#profile icon
        try:
            profile_icon = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[0]/android.widget.ImageView[0]'))
            )
            profile_icon.click()
            print("Profile Icon clicked for update the profile.")

            edit_profile_icon = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]'))
            )
            edit_profile_icon.click()
            print("Edit profile icon page opened.")

            option = random.choice(['Camera', 'Gallery'])
            print(f"Selected option: {option}")

            if option == 'Camera':
                camera_xpath = '//android.view.View[@content-desc="Camera"]'
                camera_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, camera_xpath))
                )
                camera_element.click()
                print("Camera clicked to take a picture.")
            else:
                gallery_xpath = '//android.view.View[@content-desc="Gallery"]'
                gallery_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, gallery_xpath))
                )
                gallery_element.click()
                print("Gallery option clicked to choose a picture.")


            save_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Save"]'))
            )
            save_button.click()
            print("Profile picture updated.")

            # Back to Home
            back_icon = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
            )
            back_icon.click()
            print("Profile successfully updated and back to home screen.")
        except Exception as e:
            print("Nothing happened",e)
            print(driver.page_source)

#Notification
        notification=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'))
        )
        notification.click()
        print("Notification Page open")

        back_notification=WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
        )
        back_notification.click()
        print("User back to home screen from Notification screen")

#         notification = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH,
#                                         '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'))
#         )
#         notification.click()
#         print("User again open the Notification Page.")
# #readiness notification
#         Readiness_notification_read=WebDriverWait(driver,15).until(
#             EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc= Readiness available now!]'))
#         )
#         Readiness_notification_read.click()
#         print("Notification Open for CRQ.")
#
#         back_to_subject_screen=WebDriverWait(driver,15).until(
#              EC.element_to_be_clickable((By.XPATH,'//android.widget.Button'))
#          )
#         back_to_subject_screen.click()
#         print("Back to sub screen.")
#
#         home_button = WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Home"]'))
#         )
#         home_button.click()
#         print("Home button clicked.")
#
#         notification = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH,
#                                         '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'))
#         )
#         notification.click()
#         print("Notification Page open")
#
#     #Milestone notification
#
#         Milestone_notification_read=WebDriverWait(driver,10).until(
#             EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc= "Milestone has been assigned"]')
#         ))
#         Milestone_notification_read.click()
#         print("Notification opened for milestone")
#
#         back_to_subject_screen = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.widget.Button'))
#         )
#         back_to_subject_screen.click()
#         print("Back to sub screen.")
#
#         home_button = WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Home"]'))
#         )
#         home_button.click()
#         print("Home button clicked.")
#
#         notification = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH,
#                                         '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'))
#         )
#         notification.click()
#         print("Notification Page open")
#
#     #Booster Notification
#         booster_notification=WebDriverWait(driver,15).until(
#             EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="A new booster is available"]'))
#         )
#         booster_notification.click()
#         print("Booster Notification Clicked.")
#
#         back_to_subject_screen = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.widget.Button'))
#         )
#         back_to_subject_screen.click()
#         print("Back to sub screen.")
#
#         home_button = WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Home"]'))
#         )
#         home_button.click()
#         print("Home button clicked.")
#
#         notification = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH,
#                                         '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'))
#         )
#         notification.click()
#         print("Notification Page open")
#
#     #New topic notification
#         New_topic_notification=WebDriverWait(driver,10).until(
#             EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="30 days 2 hours ago Fractions New topic has been assigned"]'))
#         )
#         New_topic_notification.click()
#         print("Topic notification clicked.")
#
#         back_to_subject_screen = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.widget.Button'))
#         )
#         back_to_subject_screen.click()
#         print("Back to sub screen.")
#
#
# #Home
#         home_button = WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="Home"]'))
#         )
#         home_button.click()
#         print("Home button clicked.")
#
#
# # Math tab
#         math_tab = WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc=" Math Tab[2] "]'))
#         )
#         math_tab.click()
#         print("Math tab clicked.")
# # Science tab
#         science_tab = WebDriverWait(driver, 30).until(
#             EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc=" Science Tab[1]"]'))
#         )
#         science_tab.click()
#         print("Science tab clicked.")
#

# #quizes

        readiness = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Readiness"]'))
        )
        readiness.click()
        print("Readiness icon clicked.")

        Cancel = '//android.widget.ScrollView/android.widget.ImageView[1]'
        cancel_start_quiz = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Cancel))
        )
        cancel_start_quiz.click()
        print("User cancel the quiz as per their choice.")

        readiness = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Readiness"]'))
        )
        readiness.click()
        print("Readiness icon clicked again.")

        start_quiz = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[contains(@content-desc, "Start")]'
))
                )
        start_quiz.click()
        print("User land to quiz screen.")
        try:
            back=WebDriverWait(driver,15).until(
                        EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="Back"]'))
                    )
            back.click()
            print("Back button Clicked instead of continuing quiz.")

            option=random.choice('Save&Quit')
            print("Selected option:",option)
            if option=='Cancel':
                cancel=WebDriverWait(driver,10).until(
                            EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Cancel"]')
                        ))
                cancel.click()
                print("User choose cancel")

                try:
                    while True:
                        print("Selecting answer options for the current question...")
                        answer_options = driver.find_elements(
                            By.XPATH,
                            "//*[@clickable='true' and (starts-with(@content-desc, 'A') or starts-with(@content-desc, 'B') or starts-with(@content-desc, 'C') or starts-with(@content-desc, 'D'))]"
                        )
                        if answer_options:
                            random_option = random.choice(answer_options)
                            random_option.click()
                            sleep(1)
                        else:
                            print("No answer options found for this question.")
                        try:
                            print("Attempting to click 'Next Question' to proceed...")
                            next_question = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//*[@content-desc='Next Question']"))
                            )
                            next_question.click()
                            sleep(1)
                        except TimeoutException:
                            print("No more questions. Quiz completed.")
                            break

                except Exception as e:
                    print("An error occurred during the quiz:", e)

            else:
                save_and_quit=WebDriverWait(driver,10).until(
                        EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Save & Quit"]')
                        ))
                save_and_quit.click()
                print("User choose save&quit to resume the readiness quizz.")

                start_resume=WebDriverWait(driver,15).until(
                        EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="Readiness"]'))
                        )
                start_resume.click()
                print("User resume the quiz.")

                cancel_resume=WebDriverWait(driver,15).until(
                        EC.element_to_be_clickable((By.XPATH,'//android.widget.ScrollView/android.widget.ImageView[1]'))
                        )
                cancel_resume.click()
                print("User canceled resume.")

                start_resume = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(
                                (By.XPATH, '//android.widget.ImageView[@content-desc="Readiness"]'))
                        )
                start_resume.click()
                print("User resume the quiz.")

                resume_tab=WebDriverWait(driver,15).until(
                            EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Resume"]'))
                        )
                resume_tab.click()
                print("User resumed the quiz")
        except Exception as e:
                print("No Action taken by user",e)
#quest
        quest=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'(//android.widget.ImageView[@content-desc="Quest"])[1]'))
        )
        quest.click()
        print("Quest open")

        Cancel = '//android.widget.ScrollView/android.widget.ImageView[1]'
        cancel_start_quiz = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Cancel))
        )
        cancel_start_quiz.click()
        print("User cancel the quest as per their choice.")

        quest = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//android.widget.ImageView[@content-desc="Quest"])[1]'))
        )
        quest.click()
        print("Quest open again after cancellation")
        start_quiz = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[contains(@content-desc, "Start")]'
                                        ))
        )
        start_quiz.click()
        print("User land to quiz screen.")
        try:
            back = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@content-desc="Back"]'))
            )
            back.click()
            print("Back button Clicked instead of continuing quiz.")

            option = random.choice('Cancel','save&quit')
            print("Selected option:", option)
            if option == 'Cancel':
                cancel = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Cancel"]')
                                               ))
                cancel.click()
                print("User choose cancel")
                try:
                    while True:
                        print("Selecting answer options for the current question.")
                        answer_options = driver.find_elements(
                            By.XPATH,
                            "//*[@clickable='true' and (starts-with(@content-desc, 'A') or starts-with(@content-desc, 'B') or starts-with(@content-desc, 'C') or starts-with(@content-desc, 'D'))]"
                        )
                        if answer_options:
                            random_option = random.choice(answer_options)
                            random_option.click()
                            sleep(1)
                        else:
                            print("No answer options found for this question.")
                        try:
                            print("Attempting to click 'Next Question' to proceed...")
                            next_question = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//*[@content-desc='Next Question']"))
                            )
                            next_question.click()
                            sleep(1)
                        except TimeoutException:
                            print("No more questions. Quiz completed.")
                            break
                except Exception as e:
                    print("An error occurred during the quiz:", e)


            else:
                save_and_quit = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Save & Quit"]')
                                               ))
                save_and_quit.click()
                print("User choose save&quit to pause the readiness quizz.")

                start_resume = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Readiness"]'))
                )
                start_resume.click()
                print("User resume the quiz.")

                cancel_resume = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]'))
                )
                cancel_resume.click()
                print("User canceled resume.")

                start_resume = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//android.widget.ImageView[@content-desc="Readiness"]'))
                )
                start_resume.click()
                print("User resume thq quiz.")

                resume_tab = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Resume"]'))
                )
                resume_tab.click()
                print("User resumed the quiz")
        except Exception as e:
            print("No Action taken by user", e)
# Milestone
        milestone=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="Milestone"]'))
        )
        milestone.click()
        print("Milestone Open")

        Cancel = '//android.widget.ScrollView/android.widget.ImageView[1]'
        cancel_start_quiz = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Cancel))
        )
        cancel_start_quiz.click()
        print("User cancel the quest as per their choice.")

        milestone = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Milestone"]'))
        )
        milestone.click()
        print("Milestone Open after canceling")

        start_quiz = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[contains(@content-desc, "Start")]'
                                        ))
        )
        start_quiz.click()
        print("User land to quiz screen.")


#Subject Screen
        subjects_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Subjects"))
        )
        subjects_button.click()
        print("Subjects button clicked.")

    # Science tab
        science_tab = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc=" Science Tab[1]"]'))
        )
        science_tab.click()
        print("Science tab clicked.")
        parent_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View'

        try:
            child_elements = driver.find_elements(By.XPATH, f"{parent_xpath}/*")

            for index, element in enumerate(child_elements, start=1):
                try:
                    content_desc = element.get_attribute("content-desc")
                    print(f"Element {index}: Content-Desc = {content_desc}")

                    element.click()
                    sleep(1)

                    driver.back()
                    sleep(1)

                except Exception as e:
                    print(f"Could not interact with element {index}. Error: {e}")

        except NoSuchElementException:
            print("No child elements found under the specified parent XPath.")
        driver.quit()

    #math tab
        math_tab = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc=" Math Tab[0]"]'))
        )
        math_tab.click()
        print("Math tab clicked.")

#Progress Screen
        progress_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Progress"))
        )
        progress_button.click()
        print("Progress button clicked.")

    #math tab
        math_tab = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc=" Math Tab[0]"]'))
        )
        math_tab.click()
        print("Math tab clicked.")

        parent_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View'

        try:
            child_elements = driver.find_elements(By.XPATH, f"{parent_xpath}/*[@content-desc]")

            for index, element in enumerate(child_elements, start=1):
                try:
                    content_desc = element.get_attribute("content-desc")
                    print(f"Element {index}: Content-Desc = {content_desc}")

                    element.click()
                    print(f"Clicked on element with content-desc: {content_desc}")
                    sleep(1)

                    driver.back()
                    sleep(1)

                except Exception as e:
                    print(f"Could not interact with element {index}. Error: {e}")

        except NoSuchElementException:
            print("No child elements found with content-desc under the specified parent XPath.")

    #science tab
        science_tab = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc=" Science Tab[1]"]'))
        )
        science_tab.click()
        print("Science tab clicked.")

        for index, element in enumerate(child_elements, start=1):
            try:
                content_desc = element.get_attribute("content-desc")
                print(f"Element {index}: Content-Desc = {content_desc}")

                if content_desc == "Ch1: Nutrition in Plants":
                    print("Performing action for Chapter 1")
                    element.click()
                elif content_desc == "CH5: Physical and Chemical Changes":
                    print("Performing action for Chapter 5")
                    element.click()
                else:
                    print("Default action for other chapters")
                    element.click()

                sleep(1)
                driver.back()
                sleep(1)

            except Exception as e:
                print(f"Could not interact with element {index}. Error: {e}")

#More screen
        more_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "More"))
        )
        more_button.click()
        print("More button clicked.")

        edit_profile=WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Edit profile"]'))
        )
        edit_profile.click()
        print("Edit profile clicked in the more screen")

        edit_profile_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]'))
        )
        edit_profile_icon.click()
        print("Edit profile icon page opened.")

        option = random.choice(['Camera', 'Gallery'])
        print(f"Selected option: {option}")

        if option == 'Camera':
            camera_xpath = '//android.view.View[@content-desc="Camera"]'
            camera_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, camera_xpath))
            )
            camera_element.click()
            print("Camera clicked to take a picture.")
        else:
            gallery_xpath = '//android.view.View[@content-desc="Gallery"]'
            gallery_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, gallery_xpath))
            )
            gallery_element.click()
            print("Gallery option clicked to choose a picture.")

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Save"]'))
        )
        save_button.click()
        print("Profile picture updated.")

        # Back to Home
        back_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
        )
        back_icon.click()
        print("Profile successfully updated and back to home screen.")

    #downloads
        Downloads=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="Downloads"]'))
        )
        Downloads.click()
        print("User clicked the downloads button to check their downloads")

        back_to_more_page=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
        )
        back_to_more_page.click()
        print("user back to more screen from downloads.")

    #raise ticket
        raise_ticket=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
        )
        raise_ticket.click()
        print("User open the raise a ticket option.")
        issue_type=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="Issue Type Select Type"]'))
        )
        issue_type.click()

        parent_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View'
        try:
            child_elements = driver.find_elements(By.XPATH, f"{parent_xpath}/*")  # Using '/*' to get all children

            for index, element in enumerate(child_elements, start=1):
                try:
                    content_desc = element.get_attribute("content-desc")
                    print(f"Element {index}: Content-Desc = {content_desc}")

                    if content_desc == "Tech":
                        print("Performing action for 'Tech'")
                        element.click()
                        sleep(1)
                        select_subject=WebDriverWait(driver,10).until(
                            EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="Subject Select Subject"]'))
                        )
                        select_subject.click()

                        option=random.choice('Science','Math')
                        print(f'Selected Options:{option}')
                        if option=='Science':
                            science=WebDriverWait(driver,10).until(
                                EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Science"]'))
                            )
                            science.click()
                        else:
                            math=WebDriverWait(driver,10).until(
                                EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Math"]'))
                            )
                            math.click()

                            description_field = driver.find_element(By.XPATH,"//android.widget.EditText[@bounds='[30,602][690,722]']")
                            description_field.click()
                            description_field.send_keys("Please provide assistance with the issue described above.")
                            print("Entered static text in the Description field.")
                            sleep(1)

                            attach_button = driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc='Attach']")
                            attach_button.click()
                            print("Clicked on the Attach button.")
                            sleep(1)

                            ticket_submit=WebDriverWait(driver,10).until(
                                EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Submit"]'))
                            )
                            ticket_submit.click()
                            print("Tech related ticket submitted.")

                    elif content_desc == "Content":
                        print("Performing action for 'Content'")
                        element.click()
                        sleep(1)

                        option = random.choice('Science', 'Math')
                        print(f'Selected Options:{option}')
                        if option == 'Science':
                            science = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Science"]'))
                            )
                            science.click()
                        else:
                            math = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Math"]'))
                            )
                            math.click()

                    elif content_desc == "Onboarding/Login":
                        print("Performing action for 'Onboarding/Login'")
                        element.click()
                        sleep(1)

                        description_field = driver.find_element(By.XPATH,
                                                                "//android.widget.EditText[@bounds='[30,602][690,722]']")
                        description_field.click()
                        description_field.send_keys("Please provide assistance with the issue described above.")
                        print("Entered static text in the Description field.")
                        sleep(1)

                        attach_button = driver.find_element(By.XPATH,
                                                            "//android.widget.ImageView[@content-desc='Attach']")
                        attach_button.click()
                        print("Clicked on the Attach button.")
                        sleep(1)

                        ticket_submit = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Submit"]'))
                        )
                        ticket_submit.click()
                        print("Onboarding/Login ticket submitted.")

                    elif content_desc == "Others":
                        print("Performing action for 'Others'")
                        element.click()
                        sleep(1)

                    else:
                        print(f"Unknown content-desc '{content_desc}' encountered. No specific action defined.")

                    driver.back()
                    sleep(1)

                except Exception as e:
                    print(f"Could not interact with element {index}. Error: {e}")

        except NoSuchElementException:
            print("No child elements found under the specified parent XPath.")

        driver.quit()

    #help center
        help_center=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="Help Center"]'))
        )
        help_center.click()
        print("User clicked the help")
        back_to_more_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
        )
        back_to_more_page.click()
        print("user back to more screen from Help.")

    # Customer Support
        customer_support=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@content-desc="Customer Support"]'))
        )
        customer_support.click()
        print("User clicked customer support.")

        back_to_more_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'))
        )
        back_to_more_page.click()
        print("user back to more screen from customer support.")

        customer_support = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@content-desc="Customer Support"]'))
        )
        customer_support.click()
        print("User clicked customer support.")












    except Exception as e:
        print(f"Error occurred: {e}")
        driver.save_screenshot("error_screen.png")
        print("Screenshot taken: error_screen.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
