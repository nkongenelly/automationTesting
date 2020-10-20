class Locators():

    # platform
    testServer = "http://app.namastefit.one/"
    chrome_extension = "E://NELLY'S FOLDERS//CODE//Python//namastefit//Selenium//namasteFit//CommonFiles//extension//extension.crx"


    # DRIVERS
    chrome_driver = "C://Python38//chromedriver.exe"
    firefox_driver = "C://Python38//geckodriver.exe"
    safari_driver = "/usr/bin/safaridriver"
    microsoft_edge_driver = "C://Python38//msedgedriver.exe"

    #chrome user profile
    chrome_user_profile = 'C://Users//nkong//AppData//Local//Google//Chrome//User Data//Default'
    firefox_user_profile = 'C://Users//nkong//AppData//Roaming//Mozilla//Firefox//Profiles//0mlir59f.default-release'

    # Page url name
    login_url = "login"
    main_url = "main"
    mysites = "mysite"
    myevents = "myevents"
    createevents = "events"
    members = "members"
    managePayments = "managePayments"

    # Google sheet
    # scope = ["https://www.googleapis.com/auth/drive"]
    # credentials = "google_sheets_credentials.json"
    # credentials = "C://Users//MB210-A30//Documents//Nelly//namaste//google_sheets_credentials.json"
    # credentials_oauth = "google_sheets_oauth.json"
    # userStoriesTestCases = "userStoriesTestCases"

    # Login page objects
    connect_with_google_xpath = '//*[@id="root"]/div/main/div[2]/div[1]/div/div[1]/a'
    # connect_with_google_xpath = '<a class="MuiButtonBase-root MuiButton-root MuiButton-text jss7" tabindex="0" aria-disabled="false" href="../auth/google"><span class="MuiButton-label"></span><span class="MuiTouchRipple-root"></span></a>'
    use_another_account_xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[6]/div/div/div[2]'
    google_email_field_id = 'identifierId'
    # google_email_field_xpath = '//*[@id="identifierId"]'
    google_emailnext_button_xpath = '//*[@id="identifierNext"]/div/button/div[2]'
    google_password_field_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
    google_passwordnext_button_xpath = '//*[@id="passwordNext"]/div/button/div[2]'

    # email_field_id = "form-signin-email"
    # pass_field_id = "form-signin-password"
    # login_button_xpath = "//*[@id='formLogin']/button"
    namaste_logo_xpath = "//*[@id='mainLogo']"
    successful_login_indicator_id = "getStarted"
    successful_login_logo_xpath = '//*[@id="root"]/div/div/header/div/div/img'
    signout_button_xpath = '//*[@id="root"]/div/div/nav/div[2]/div/div/div/div[2]/button/span[1]'

    #signout
    signout_button_xpath = '//*[@id="root"]/div/div/nav/div[2]/div/div/div/div[2]/button/span[1]'
    # valid login
    namaste_username = "nelly@namaste.fit"
    namaste_password = "qwertyui"

    # Landing page objects
    mysite_button_id = "mySite"
    mysite_button_text = "My Site"
    mysite_button_text_xpath = '//*[@id="page-content-wrapper"]/div/div[1]/h4'
    get_started_text_xpath = "/html/div/div[2]/div/div[1]/h4"
    get_started_text_text = "Get Started"
    customize_my_site_button_xpath = '//*[@id="siteCustomize"]/div/div[2]/h4'
    customize_my_site_button_text = 'Customize your site'
    setup_events_button_xpath ='//*[@id="eventsSetup"]/div/div[2]/h4'
    setup_events_button_text ='Setup Events'
    my_events_button_id = "overview"
    my_events_button_text = "My Events"
    my_events_button_text_xpath = '//*[@id="page-content-wrapper"]/div/div[1]/h4'
    members_button_id = "members"
    members_button_text = "Summary"
    members_button_text_xpath = '//*[@id="page-content-wrapper"]/div/div[1]/h4'
    create_events_button_id = "events"
    create_events_button_text = "Create Event"
    create_events_button_text_xpath = '//*[@id="screenTitle"]'
    manage_payments_id = "managePayments"
    manage_payments_text = "Payment Methods"
    manage_payments_text_xpath = '//*[@id="screenTitle"]'

    # My site page
    my_site_page_text_xpath = '//*[@id="page-content-wrapper"]/div/div[1]/h4'
    preview_button_id = "previewDomain"
    studio_name_id = "name"
    studio_description_id = "about"
    city_field_id = "city"
    state_field_id = "state"
    country_state_id = "country"

    #mysite page objects

    instagram_textbox_id = "instagram"
    facebook_textbox_id = "facebook"
    youtube_textbox_id = "youtube"
    website_textbox_id = "website"
    publish_button_xpath = '//*[@id="customForm"]/form/div/div[6]/div/div/button'
    publish_button_xpath = '//*[@id="customForm"]/form/div/div[6]/div/div/button'

    # Landing page objects

    #mobile emulation
    chrome_mobile_emulation = {
    "deviceName": "Galaxy S5"
    # "deviceName": "Pixel 2",
    # "deviceName": "Pixel 2 XL",
    # "deviceName": "iPhone 5/SE",
    # "deviceName": "iPhone 6/7/8",
    # "deviceName": "iPhone 6/7/8 Plus",
    # "deviceName": "iPhone X",
    # "deviceName": "iPad",
    # "deviceName": "iPad Pro",
    }

