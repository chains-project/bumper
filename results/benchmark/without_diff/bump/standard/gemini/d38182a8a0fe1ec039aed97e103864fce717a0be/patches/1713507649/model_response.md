```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void testScope() {
    final java.lang.String line = "GET /resource.txt HTTP/1.1";
    final java.lang.String action = "foo:bar:baz";
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> caction = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> cline = new java.util.concurrent.atomic.AtomicReference<>();

    final java.util.regex.Pattern pattern = java.util.regex.Pattern.compile(
            "^(\\S+)\\s(\\S+)\\s(\\S+)\\s?(.*)$"
    );

    final java.util.regex.Matcher matcher = pattern.matcher(line);
    if (matcher.find()) {
        caction.set(matcher.group(1));
        cline.set(matcher.group(2));
    }

    org.junit.jupiter.api.Assertions.assertEquals(action, caction.get());
    org.junit.jupiter.api.Assertions.assertEquals(line, cline.get());
}
```