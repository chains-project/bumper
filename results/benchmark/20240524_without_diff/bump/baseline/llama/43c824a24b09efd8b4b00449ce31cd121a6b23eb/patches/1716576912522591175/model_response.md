```java
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonMappingException;

public JsonNode jsonBranchToJsonNode(JsonBranch jsonBranch) {
    ObjectMapper mapper = new ObjectMapper();
    try {
        return mapper.readTree(jsonBranch.toString());
    } catch (JsonMappingException e) {
        throw new RuntimeException(e);
    }
}
```