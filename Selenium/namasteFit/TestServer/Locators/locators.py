class Locators():

    # platform
    testServer = "http://app.raawmove.com/"

    # DRIVERS
    chrome_driver = "C://Python38//chromedriver.exe"
    firefox_driver = "C://Python38//geckodriver.exe"
    safari_driver = "/usr/bin/safaridriver"
    microsoft_edge_driver = "C://Python38//msedgedriver.exe"

    # Page url name
    login_url = "login"
    main_url = "main"

    # Google sheet
    scope = ["https://www.googleapis.com/auth/drive"]
    credentials = "google_sheets_credentials.json"
    credentials_oauth = "google_sheets_oauth.json"
    userStoriesTestCases = "userStoriesTestCases"

    # Login page objects
    email_field_id = "form-signin-email"
    pass_field_id = "form-signin-password"
    login_button_xpath = "//*[@id='formLogin']/button"
    namaste_logo_xpath = "//*[@id='mainLogo']"
    successful_login_indicator_id = "getStarted"
    signout_button_xpath = "signOut"

    #mysite page objects
    instagram_textbox_id = "instagram"
    facebook_textbox_id = "facebook"
    youtube_textbox_id = "youtube"
    website_textbox_id = "website"
    publish_button_xpath = '//*[@id="customForm"]/form/div/div[6]/div/div/button'

    # Landing page objects
    mysite_button_id = "mySite"
    get_started_text_xpath = "/html/div/div[2]/div/div[1]/h4"