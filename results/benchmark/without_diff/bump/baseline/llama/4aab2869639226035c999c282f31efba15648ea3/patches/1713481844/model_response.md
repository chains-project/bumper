Here's a possible patch to fix the error:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
The patch removes the `YamlPolicyFactory` import, which is not available in the dependencies listed. Instead, it uses the `Yaml` class from the `com.artipie.security.policy` package to read the YAML configuration.

Here's the patch in code format:
```diff
-@Override
-public Policy<?> getPolicy(final PolicyConfig config) {
-    final PolicyConfig sub = config.config("storage");
-    try {
-        return new YamlPolicy(
-            new BlockingStorage(
-                new Storages().newStorage(
-                    sub.string("type"), YamlPolicyFactory.createYamlInput(sub.toString())
-            )
-        );
-    } catch (final IOException err) {
-        throw new UncheckedIOException(err);
-    }
-}
+@Override
+public Policy<?> getPolicy(final PolicyConfig config) {
+    final PolicyConfig sub = config.config("storage");
+    try {
+        return new YamlPolicy(
+            new BlockingStorage(
+                new Storages().newStorage(
+                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
+            )
+        );
+    } catch (final IOException err) {
+        throw new UncheckedIOException(err);
+    }
+}
```