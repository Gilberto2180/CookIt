const nose = async () => {
    const url = "https://cookit-j5x3.onrender.com/auth/o/google-oauth2/?state=eaJR4BKLWKV6ePc6oBGEPoO8AmZSO91w&code=4%2F0AdLIrYf-DhomJph1bLk4DSYIumIVe52JvnbWRITmeTewRl5VU96prwGNI95XGFj7jxj8og"
    const response = await fetch(url, {
        method: "POST"
    })

    const n = await response.json()

    console.log(n)
}

nose()
