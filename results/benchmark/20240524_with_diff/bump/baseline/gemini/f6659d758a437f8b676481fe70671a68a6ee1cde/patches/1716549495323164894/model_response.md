```java
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.parser.ParserImpl;
import org.yaml.snakeyaml.reader.StreamReader;

import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.nio.charset.Charset;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

public class AbstractTest {
    private static final Pattern YAML_HEADER_PATTERN = Pattern.compile("^\\ufeff?%YAML[:\\s](1\\.[0-2]|1\\.[1-2])\\s*$");

    public void testYamlParserWithCustomTag() throws IOException {
        InputStream inputStream = this.getClass().getResourceAsStream("/data/yaml/custom-tag.yaml");
        Reader reader = new StreamReader(inputStream, Charset.defaultCharset());
        ParserImpl parser = new ParserImpl();
        parser.setAllowUnicode(true);
        parser.setEncoding(Charset.defaultCharset().name());
        parser.setVersion(reader.peek() == 0xFEFF ? 1 : 2);
        parser.setTags(getCustomTags());
        parser.parse(reader);
    }

    private List<Tag> getCustomTags() {
        return List.of(new Tag("!foo", Pattern.compile("^foo:\\s.*$")));
    }

    public void testYamlParserWithCustomTagAndGlobalTag() throws IOException {
        InputStream inputStream = this.getClass().getResourceAsStream("/data/yaml/custom-tag-global.yaml");
        Reader reader = new StreamReader(inputStream, Charset.defaultCharset());
        ParserImpl parser = new ParserImpl();
        parser.setAllowUnicode(true);
        parser.setEncoding(Charset.defaultCharset().name());
        parser.setVersion(reader.peek() == 0xFEFF ? 1 : 2);
        parser.setTags(getCustomTags());
        parser.setGlobalTag(new Tag("!global", Pattern.compile("^global:\\s.*$")));
        parser.parse(reader);
    }

    public void testYamlParserWithCustomTagAndGlobalTagAndInspector() throws IOException {
        InputStream inputStream = this.getClass().getResourceAsStream("/data/yaml/custom-tag-global-inspector.yaml");
        Reader reader = new StreamReader(inputStream, Charset.defaultCharset());
        ParserImpl parser = new ParserImpl();
        parser.setAllowUnicode(true);
        parser.setEncoding(Charset.defaultCharset().name());
        parser.setVersion(reader.peek() == 0xFEFF ? 1 : 2);
        parser.setTags(getCustomTags());
        parser.setGlobalTag(new Tag("!global", Pattern.compile("^global:\\s.*$")));
        parser.setInspector(new CustomTagInspector());
        parser.parse(reader);
    }

    private static class CustomTagInspector extends TrustedTagInspector {
        public CustomTagInspector() {
            super(List.of("!foo", "!global"));
        }

        @Override
        public boolean isGlobalTagAllowed(Tag tag) {
            return tag.matches("!global");
        }
    }
}
```