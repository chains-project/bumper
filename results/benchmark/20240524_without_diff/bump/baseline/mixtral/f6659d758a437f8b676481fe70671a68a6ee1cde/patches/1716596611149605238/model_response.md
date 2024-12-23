Here's a possible patch for the given code. I made some assumptions since the error message doesn't provide enough context about the specific symbol that cannot be found:

```java
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.databind.jsontype.impl.TypeDeserializerBasedJavaType;
import com.fasterxml.jackson.datatype.jdk8.Jdk8Module;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import com.fasterxml.jackson.module.paramnames.ParameterNamesModule;
import org.yaml.snakeyaml.Loader;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.nodes.Tag;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.ZoneId;
import java.time.LocalDate;
import java.util.LinkedHashMap;
import java.util.Map;

public <T extends MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    ObjectMapper objectMapper = new ObjectMapper()
            .registerModule(new ParameterNamesModule())
            .registerModule(new Jdk8Module())
            .registerModule(new JavaTimeModule());

    LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setAllowDuplicateKeys(true);
    loadingConfig.setMaxAliasesForCollections(1024);

    Map<Class<?>, Tag> tagToClass = new LinkedHashMap<>();
    tagToClass.put(ZoneId.class, new Tag("!ZoneId"));
    tagToClass.put(LocalDate.class, new Tag("!LocalDate"));

    Loader loader = new Loader(new Constructor(loadingConfig) {
        @Override
        protected JavaType _typeFromId(Tag tag) {
            Class<?> type = tagToClass.get(tag.getValue());
            if (type != null) {
                return TypeDeserializerBasedJavaType._from(objectMapper.getTypeFactory(), type);
            }
            return super._typeFromId(tag);
        }
    });

    Yaml yaml = new Yaml(loader);

    try {
        JsonNode jsonNode = yaml.load(new BufferedReader(new FileReader(path)));
        return objectMapper.treeToValue(jsonNode, clazz);
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
}
```

This solution uses Jackson's ObjectMapper to parse the YAML file, which is then converted to a JsonNode. After that, the JsonNode is converted to the desired class using the ObjectMapper.

In order to support the custom tags for ZoneId and LocalDate, the Loader constructor is overridden to handle the custom tags during deserialization.

Note that you should replace any missing imports if necessary.