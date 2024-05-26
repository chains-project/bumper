Here is the proposed patch:

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

In this patch, I created a new variable `notContains` to store the boolean value returned by the `contains` method. Then, I used the not operator `!` to negate the value of `notContains` and passed it as the first argument to the `StringContains` constructor. If `notContains` is true, then the first argument to `StringContains` will be an empty string, and if `notContains` is false, then the first argument will be null. This should fix the error message you provided.