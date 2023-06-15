console.log("Hello Muskervite's")

const alerts = document.querySelectorAll('.alert')
alerts.forEach(function (alert) {
  new bootstrap.Alert(alert)

  let alert_timeout = alert.getAttribute('data-timeout')
  setTimeout(() => {
    bootstrap.Alert.getInstance(alert).close()
  }, +alert_timeout)
})
