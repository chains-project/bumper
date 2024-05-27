Here's a fixed version of the code:

```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image)));
}
```

The issue was caused by passing two arguments to `StringContains` constructor, while it only accepts a single `String` argument. I removed the `false` argument from the constructor call.