Here is the proposed patch for the failing client code:
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
The failure is caused by the change in the `org.hamcrest.core.StringContains` constructor, which now requires a single `String` argument instead of a `boolean` and a `String`. To fix the issue, I have created a separate variable `contains` to store the result of the `output.contains` method, and then used a ternary operator to conditionally create the argument for the `StringContains` constructor based on the value of `contains`.