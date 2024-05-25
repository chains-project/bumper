```java
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.fge.jsonpatch.JsonPatch;
import com.github.fge.jsonpatch.JsonPatchException;
import de.gwdg.metadataqa.api.json.JsonBranch;
import de.gwdg.metadataqa.api.json.JsonPatcher;
import de.gwdg.metadataqa.api.json.JsonPatcherFactory;
import de.gwdg.metadataqa.api.json.JsonPatcherFactoryImpl;
import de.gwdg.metadataqa.api.json.JsonPatcherImpl;
import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MarcFactory {

    private static final Logger log = LoggerFactory.getLogger(MarcFactory.class);
    private static final JsonPatcherFactory jsonPatcherFactory = new JsonPatcherFactoryImpl();
    private static final ObjectMapper objectMapper = new ObjectMapper();

    public static Optional<JsonBranch> createMarcBranch(String jsonPatchString) {
        try {
            JsonPatch jsonPatch = JsonPatch.fromJson(jsonPatchString);
            JsonNode jsonNode = objectMapper.readTree("{}");
            JsonPatcher jsonPatcher = jsonPatcherFactory.create(jsonNode);
            JsonNode patchedJsonNode = jsonPatcher.apply(jsonPatch);
            return Optional.of(new JsonBranch(patchedJsonNode));
        } catch (IOException | JsonPatchException e) {
            log.error("Error creating MARC branch from JSON patch string: {}", e.getMessage());
            return Optional.empty();
        }
    }

    public static Optional<JsonBranch> createMarcBranch(List<String> jsonPatchStrings) {
        if (jsonPatchStrings == null || jsonPatchStrings.isEmpty()) {
            return Optional.empty();
        }

        try {
            List<JsonPatch> jsonPatches = jsonPatchStrings.stream()
                    .map(JsonPatch::fromJson)
                    .collect(Collectors.toList());

            JsonNode jsonNode = objectMapper.readTree("{}");
            JsonPatcher jsonPatcher = jsonPatcherFactory.create(jsonNode);

            for (JsonPatch jsonPatch : jsonPatches) {
                jsonNode = jsonPatcher.apply(jsonPatch);
            }

            return Optional.of(new JsonBranch(jsonNode));
        } catch (IOException | JsonPatchException e) {
            log.error("Error creating MARC branch from JSON patch strings: {}", e.getMessage());
            return Optional.empty();
        }
    }

    public static Optional<JsonBranch> createMarcBranch(String... jsonPatchStrings) {
        return createMarcBranch(List.of(jsonPatchStrings));
    }

    public static Optional<JsonBranch> createMarcBranch() {
        return createMarcBranch(Collections.emptyList());
    }
}
```