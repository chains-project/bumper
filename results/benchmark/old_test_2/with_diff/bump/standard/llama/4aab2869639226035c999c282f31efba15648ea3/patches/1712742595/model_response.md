Here's a proposed patch to fix the error:
```diff
-@java.lang.Override
-public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
-    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
-    try {
-        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
-    } catch (final java.io.IOException err) {
-        throw new java.io.UncheckedIOException(err);
-    }
-}
+@java.lang.Override
+public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
+    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
+    try {
+        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(com.artipie.asto.factory.Storages.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
+    } catch (final java.io.IOException err) {
+        throw new java.io.UncheckedIOException(err);
+    }
+}
```
The patch replaces the line `return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));`
with `return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(com.artipie.asto.factory.Storages.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));`.


The patch uses the `com.artipie.asto.factory.Storages` class instead of `com.artipie.security.policy.Storages` to create the `Storage` instance, as the latter is not available in the updated library version. The `com.artipie.asto.factory.Storages` class provides the same functionality and can be used as a replacement.

Note that this patch only addresses the reported error and does not take into account any potential issues with the rest of the code. It's important to test the patch thoroughly to ensure it does not introduce any new errors.