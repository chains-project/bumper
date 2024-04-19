```java
import de.gwdg.metadataqa.api.json.JsonElement;

  public class MarcFactory {

    public static JsonElement createJsonElement(String json) {
      return JsonElement.parse(json);
    }

  }
```