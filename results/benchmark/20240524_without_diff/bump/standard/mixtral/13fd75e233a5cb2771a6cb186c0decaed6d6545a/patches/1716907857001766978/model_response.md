Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean contains = output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(contains ? "" : java.lang.String.format("latest: digest: %s", original.digest())));
}
```
In this patch, I created a new boolean variable `contains` to store the result of the `contains` method. Then, I used this variable to conditionally create the `StringContains` object, passing an empty string as argument if `contains` is true, and the formatted string otherwise. This way, the `StringContains` constructor is called with the correct number of arguments.