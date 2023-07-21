def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\bFound an existing installation of Pyrogram...\nSuccessfully Imported.\n\n"
    except BaseException:
        print("Installing Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bDone. Installed and imported Pyrogram."
        from pyrogram import Client
        
    clear_screen()
    print(ULTROID)
    print(x)

    # generate a session
    API_ID, API_HASH = get_api_id_and_hash()
    print("Enter phone number when asked.\n\n")
    try:
        with Client(name="ultroid", api_id=API_ID, api_hash=API_HASH, in_memory=True) as pyro:
            ss = pyro.export_session_string()
            pyro.send_message(
                "me",
                f"`{ss}`\n\nAbove is your Pyrogram Session String for @TheUltroid. **DO NOT SHARE it.**",
            )
            print("Session has been sent to your saved messages!")
            exit(0)
    except Exception as er:
      print("Unexpected error occurred while creating session, make sure to validate your inputs.")
      print(er)
