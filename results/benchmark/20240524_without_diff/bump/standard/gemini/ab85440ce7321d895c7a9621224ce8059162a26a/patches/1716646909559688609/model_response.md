```java
final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), org.hamcrest.Matchers.equalTo(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), org.hamcrest.Matchers.allOf(java.util.Arrays.asList(org.hamcrest.Matchers.containsString("Invalid tag"), org.hamcrest.Matchers.not(org.hamcrest.Matchers.containsString(original)))));
```