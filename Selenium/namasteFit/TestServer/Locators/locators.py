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
    # credentials = "google_sheets_credentials.json"
    credentials = "C://Users//MB210-A30//Documents//Nelly//namaste//google_sheets_credentials.json"
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
    mysite_button_text = "My Site"
    get_started_text_xpath = "/html/div/div[2]/div/div[1]/h4"
    get_started_text_text = "Get Started"
    customize_my_site_button_xpath = '//*[@id="siteCustomize"]/div/div[2]/h4'
    customize_my_site_button_text = 'Customize your site'
    setup_events_button_xpath ='//*[@id="eventsSetup"]/div/div[2]/h4'
    setup_events_button_text ='Setup Events'
    my_events_button_id = "overview"
    my_events_button_text = "My Events"
    members_button_id = "members"
    members_button_text = "Members"