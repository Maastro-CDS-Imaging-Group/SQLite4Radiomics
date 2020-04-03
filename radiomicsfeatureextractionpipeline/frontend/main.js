const { app, BrowserWindow } = require('electron')

let win;

function createWindow() {
    //create browser window
    win = new BrowserWindow({
        width: 600,
        height: 600,
        backgroundColor: '#ffffff',
        webPreferences: {
            nodeIntegration: true
        },
        icon: './radboudumc.ico'
    })
    win.setMenu(null)

    win.maximize()

    win.loadURL(`file://${__dirname}/dist/index.html`)


    const ses = win.webContents.session

    ////uncomment below to open devtools
    //win.webContents.openDevTools()

    //Event when the window is closed
    win.on('closed', function() {
        win = null
    })
}

// create window on electron initialization
app.on('ready', createWindow)

// quit when all windows are closed
app.on('window-all-closed', function(){
    //on macOS specific close process
    if(process.platform = 'darwin'){
        app.quit()
    }
})

app.on('activate', function(){
    //macOS specific open process
    if(win === null) {
        createWindow()
    }
})