```java
  import org.bouncycastle.crypto.tls.AlertDescription;

  import java.util.HashMap;
  import java.util.Map;

  public class ChachaDecoder {

      private static final Map<Short, AlertDescription> ALERT_DESCRIPTION_MAP = new HashMap<>();

      static {
          ALERT_DESCRIPTION_MAP.put((short) 40, AlertDescription.illegal_parameter);
          ALERT_DESCRIPTION_MAP.put((short) 47, AlertDescription.unknown_psk_identity);
          // Add other alert descriptions as needed
      }

      public void decode(byte[] message) {
          // ... existing code ...

          short alertLevel = message[0];
          short alertDescription = message[1];

          AlertDescription description = ALERT_DESCRIPTION_MAP.get(alertDescription);
          if (description == null) {
              // Handle unknown alert descriptions
              System.out.println("Unknown alert description: " + alertDescription);
          } else {
              // Handle known alert descriptions
              System.out.println("Alert description: " + description);
          }

          // ... existing code ...
      }
  }
```