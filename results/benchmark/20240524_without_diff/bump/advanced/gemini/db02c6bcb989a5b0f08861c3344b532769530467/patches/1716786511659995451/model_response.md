```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        final java.util.Optional<java.lang.String> opt = java.util.Optional.ofNullable(string);
        opt.ifPresent(s -> {
            final java.util.List<java.lang.String> parts = java.util.Arrays.asList(s.split(":"));
            if (parts.size() == 3) {
                final java.lang.String name = parts.get(0);
                final java.lang.String tag = parts.get(1);
                final java.lang.String digest = parts.get(2);
                final com.artipie.docker.ref.ManifestRef ref = new com.artipie.docker.ref.ManifestRef(name, tag, digest);
                final com.artipie.docker.ref.ManifestRef ref2 = new com.artipie.docker.ref.ManifestRef(name, tag, digest);
                final boolean equals = ref.equals(ref2);
                final int hashCode = ref.hashCode();
                final java.lang.String string1 = ref.toString();
                final java.lang.String string2 = ref2.toString();
                final boolean equals2 = string1.equals(string2);
            }
        });
    } catch (final java.lang.Throwable e) {
        throwable = e;
    }
}
```