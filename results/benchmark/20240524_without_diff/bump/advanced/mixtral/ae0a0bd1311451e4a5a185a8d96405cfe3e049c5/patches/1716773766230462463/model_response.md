Here's the proposed patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void shouldPush() throws java.lang.Exception {
    final com.artipie.docker.http.Image original = new com.artipie.docker.http.Image.ForOs();
    final java.lang.String image = this.copy(original);
    final java.lang.String output = this.cli.run("push", image);
    boolean containsDigest = output.contains(String.format("latest: digest: %s", original.digest()));
    org.hamcrest.MatcherAssert.assertThat(output, new org.hamcrest.core.StringContains("latest: digest: " + original.digest()));
}
```

The failure is caused by the wrong usage of `org.hamcrest.core.StringContains`. I replaced it with a new instance, constructed with the expected substring. Additionally, I created a separate variable `containsDigest` to store the result of the `contains` method, to make the code cleaner.