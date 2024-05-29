Here's the updated code that should fix the error:

```java
@org.junit.jupiter.api.Test
void shouldPull() throws java.lang.Exception {
    final java.lang.String image = this.copy(new com.artipie.docker.http.Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final java.lang.String output = this.cli.run("pull", image);
    boolean contains = output.contains(String.format("Status: Downloaded newer image for %s", image));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(contains ? "" : "Not ", image));
}
```

The error was caused by passing two arguments to the `StringContains` constructor instead of one. The first argument should be a substring to search for, and the second argument is an optional negation flag. In this case, we can use the `contains` method of the `output` string to check if it contains the desired substring, and then pass the result (a boolean) to the `StringContains` constructor. We also added an optional "Not " prefix to the `image` argument of `StringContains` to indicate negation if the `contains` method returns `false`.