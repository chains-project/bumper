Here's the patched version of your code. I created a `TrustedTagInspector` class to fix the error since it's not found in the external dependency.

```java
import com.premiumminds.billy.core.test.fixtures.JavaZoneIdConstruct;
import com.premiumminds.billy.core.test.fixtures.JavaLocalDateConstruct;
import org.yaml.snakeyaml.*;
import org.yaml.snakeyaml.nodes.*;
import java.io.*;
import java.time.*;

public <T extends com.premiumminds.billy.core.test.fixtures.MockBaseEntity> T createMockEntity(Class<T> clazz, String path) {
    final LoaderOptions loadingConfig = new LoaderOptions();
    loadingConfig.setTagInspector(new TrustedTagInspector());
    final Representer representer = new Representer(new DumperOptions());
    final Tag zoneIdTag = new Tag("!ZoneId");
    representer.addClassTag(ZoneId.class, zoneIdTag);
    final Tag localDateTag = new Tag("!LocalDate");
    representer.addClassTag(LocalDate.class, localDateTag);
    final Constructor constructor = new Constructor(clazz, loadingConfig) {{
        addTypeDescription(new TypeDescription(ZoneId.class, "ZoneId"));
        addTypeDescription(new TypeDescription(LocalDate.class, "LocalDate"));
        yamlConstructors.put(zoneIdTag, new JavaZoneIdConstruct());
        yamlConstructors.put(localDateTag, new JavaLocalDateConstruct());
    }};
    Yaml yaml = new Yaml(constructor, representer);
    try {
        return yaml.load(new BufferedReader(new FileReader(path)));
    } catch (FileNotFoundException e) {
        throw new RuntimeException(e);
    }
}

static class TrustedTagInspector extends SafeConstructor.SafeTagInspector {
    @Override
    public boolean isTrusted(Tag tag) {
        return true;
    }
}
```

This patch creates the `TrustedTagInspector` class as an inner class of the `AbstractTest` class, extending `SafeConstructor.SafeTagInspector` and overriding the `isTrusted` method to always return `true`. This way, the `LoaderOptions` instance will use this custom `TrustedTagInspector` to avoid the "cannot find symbol" error.