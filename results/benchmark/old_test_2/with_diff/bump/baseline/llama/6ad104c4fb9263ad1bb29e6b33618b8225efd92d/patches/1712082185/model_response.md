Here's a possible patch to fix the failure:
```
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...
    TlsFatalAlert tlsFatalAlert = new TlsFatalAlert(AlertDescription.close_notify);
    // ...
}
```
Replace the failing line with the following code:
```
TlsFatalAlert tlsFatalAlert = new TlsFatalAlert(AlertDescription.close_notify, org.bouncycastle.crypto.tls.TlsFatalAlert.getAlertDescription());
```
The `getAlertDescription()` method has been removed in the new version of the library, so we need to use the constructor that takes a `short` parameter instead. We also need to call `TlsFatalAlert.getAlertDescription()` to get the alert description, as the `getAlertDescription()` method is not available anymore.

Note that this patch assumes that the `AlertDescription` class is still available in the new version of the library. If it's not, you may need to adjust the code accordingly.