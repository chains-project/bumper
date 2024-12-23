```java
import org.bouncycastle.crypto.tls.AlertLevel;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void handle(byte[] message) {
        // Check the message type
        if (message[0] == AlertLevel.fatal) {
            // Get the alert description
            short alertDescription = (short) (message[1] & 0xff);

            // Create a new TlsFatalAlert object
            TlsFatalAlert fatalAlert = new TlsFatalAlert(alertDescription);

            // Handle the alert
            handleAlert(fatalAlert);
        }
    }

    private void handleAlert(TlsFatalAlert fatalAlert) {
        // Handle the alert based on its description
        switch (fatalAlert.getAlertDescription()) {
            case AlertDescription.close_notify:
                // Handle close notify alert
                break;
            case AlertDescription.unexpected_message:
                // Handle unexpected message alert
                break;
            // Add other alert handling cases as needed
            default:
                // Handle unknown alert
                break;
        }
    }
}
```