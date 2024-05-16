const activate = async (uid, token) => {
    const url = "https://cookit-j5x3.onrender.com/auth/users/activation/"
    
    console.log(uid)
    console.log(token)
    
    const body = {
        uid,
        token,
    }
    const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
            "Content-Type": "application/json"
        }
    })

    const content = document.getElementById("info")

    if (response.status === 204) {
        content.innerHTML = "Cuenta activada! Regrese a la aplicacion"
    } else {
        content.innerHTML = "Su cuenta ya encuentea activa, regrese a la aplicacion"
    }
}
