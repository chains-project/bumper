Here's a possible patch that fixes the error by using the `containsString` method from Hamcrest 2.x:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.provider.ValueSource;

class TagValidTest {

    @Test
    @ValueSource(strings = {
        "",
        ".0",
        "*",
        "\u00ea",
        "-my-tag",
        //@checkstyle LineLengthCheck (1 line)
        "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678"
    })
    void shouldFailToGetValueWhenInvalid(final String original) {
        final Tag.Valid tag = new Tag.Valid(original);
        assertThat(tag.valid(), new IsEqual<>(false));
        assertThrows(InvalidTagNameException.class, tag::value);
        final Throwable throwable = assertDoesNotThrow(() -> tag.value());
        assertThat(throwable, not(containsString(original)));
        assertThat(throwable.getMessage(), containsString("Invalid tag"));
    }
}
```

The changes made are:

1. Importing the `containsString` and `not` matchers from `org.hamcrest.Matchers`.
2. Using `assertDoesNotThrow` instead of `assertThrows` to check that the `tag.value()` call does not throw an exception.
3. Using `not(containsString(original))` instead of `new StringContains(false, original)` to check that the exception message does not contain the original string.
4. Using `containsString("Invalid tag")` instead of `new StringContains(true, "Invalid tag")` to check that the exception message contains the string "Invalid tag".