Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean notContains = !output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains(notContains ? "" : null, java.lang.String.format("latest: digest: %s", original.digest())));
}
```
In this patch, we first compute the value of `notContains` as the negation of the result of calling `contains` on the `output` string. We then pass `notContains` as the first argument to `StringContains`, and pass `null` as the second argument if `notContains` is `false`, and an empty string if `notContains` is `true`. This should satisfy the constructor of `StringContains`, which expects a boolean as its first argument and a string as its second argument.