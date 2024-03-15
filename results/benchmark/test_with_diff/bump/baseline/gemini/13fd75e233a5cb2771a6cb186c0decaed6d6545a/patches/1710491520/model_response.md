```java
void shouldFailToGetValueWhenInvalid(final String original) {
        final Tag.Valid tag = new Tag.Valid(original);
        MatcherAssert.assertThat(tag.valid(), new IsEqual<>(false));
        final Throwable throwable = Assertions.assertThrows(
            InvalidTagNameException.class,
            tag::value
        );
        MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                Arrays.asList(
                    new StringContains(true, "Invalid tag"),
                    new StringContains(true, original)
                )
            )
        );
    }
```