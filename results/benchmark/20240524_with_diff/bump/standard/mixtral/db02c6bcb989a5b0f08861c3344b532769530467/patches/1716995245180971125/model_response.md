Here's a fixed version of the code that should work with the new library version:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains.ContainsSubstring(java.lang.String.format("latest: digest: %s", original.digest())));
}
```

In the original code, the `StringContains` constructor was being called with two arguments, but the updated library version only accepts one argument. To fix this, I replaced `StringContains` with `StringContains.ContainsSubstring`, which accepts a single `String` argument representing the substring to search for.