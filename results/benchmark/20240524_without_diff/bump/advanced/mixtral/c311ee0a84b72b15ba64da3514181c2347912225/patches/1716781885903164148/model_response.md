Here's the fixed version of the code:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean notExpected = false;
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(notExpected, java.lang.String.format("latest: digest: %s", original.digest())));
}
```

The issue was caused by passing a boolean value to the `StringContains` constructor, which expects a `String` instead. I added a new variable `notExpected` of type `boolean` and passed it as the first argument to the `StringContains` constructor.