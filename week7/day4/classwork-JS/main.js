//build function to get token
const getAuth = async () => {
    const clientID = '940ca0e54fbb43de8f24d3d57388c089'
    const clientSecret = '87de30c714ca41a9a305b4e41a1a78fb'
    const response = await fetch('https://accounts.spotify.com/api/token', {

        method: 'POST',
        headers: {
            'Authorization': 'Basic ' + (new Buffer(clientID + ':' + clientSecret).toString('base64'))
          },
          form: {
            grant_type: 'client_credentials'
          },
          json: true
    })
    const token = await response.json()
    console.log(token)
}

getAuth()