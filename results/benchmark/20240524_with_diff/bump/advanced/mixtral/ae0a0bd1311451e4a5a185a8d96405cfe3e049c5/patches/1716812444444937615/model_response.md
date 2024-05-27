Here's the updated code to fix the error:

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

The issue was caused by the `StringContains` constructor, which now expects only one argument (a `String`), but previously accepted two arguments (a `boolean` and a `String`). In the updated code, I have removed the `false` argument from the `StringContains` constructor.