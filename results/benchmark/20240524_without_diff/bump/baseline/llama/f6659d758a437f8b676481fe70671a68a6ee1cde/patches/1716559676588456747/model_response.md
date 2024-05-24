```
import org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector;

TrustedPrefixesTagInspector inspector = new TrustedPrefixesTagInspector(java.util.Arrays.asList("tag:yaml.org,2002:map", "tag:yaml.org,2002:seq", "tag:yaml.org,2002:str"));
```