```java
package org.junit;

import java.util.Arrays;

import static java.lang.System.arraycopy;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.fail;
import static org.junit.Assume.assumeFalse;
import static org.junit.Assume.assumeNoException;
import static org.junit.Assume.assumeNotNull;
import static org.junit.Assume.assumeThat;
import static org.junit.Assume.assumeTrue;

/**
 * A set of assumptions about the current environment. Can be used with
 * {@link org.junit.rules.TestRule}s to skip a test if an assumption fails.
 *
 * <p>Here are some examples of using assumptions:
 * <pre>
 * public static class Assumptions {
 *   @Rule
 *   public TestWatcher watcher= new TestWatcher() {
 *     protected void failed(Throwable e, Description description) {
 *       Assume.assumeNoException("Found a bug in " + description.getDisplayName(), e);
 *     }
 *   };
 *
 *   @Test public void testOnlyOnAThursday() {
 *     Assume.assumeThat(new Date().getDay(), is(Calendar.THURSDAY));
 *     // Test passes only on Thursdays
 *   }
 *
 *   @Test public void testOnWindowsOnly() {
 *     Assume.assumeTrue(System.getProperty("os.name").startsWith("Windows"));
 *     // Test passes only on Windows
 *   }
 *
 *   @Test public void testNotOnAFriday() {
 *     Assume.assumeFalse("Skipping test on Friday", new Date().getDay() == Calendar.FRIDAY);
 *     // Test passes only on non-Fridays
 *   }
 * }
 * </pre>
 *
 * <p>In order to implement your own assumptions you can subclass this class
 * and override {@link #toAssumption(boolean, String)}
 * and {@link #handleAssumptionViolated(org.junit.AssumptionViolatedException)}.
 * You can then use your assumption class in the same way as the standard
 * assumptions provided in this class.
 *
 * @since 4.0
 */
public class Assume {
    /**
     * Fails a test if the given condition is false.
     *
     * @param condition the condition to evaluate
     *
     * @see #assumeThat(boolean, String, org.hamcrest.Matcher)
     */
    public static void assumeTrue(boolean condition) {
        assumeThat(condition, is(true), "expected: true but was: false");
    }

    /**
     * Fails a test if the given condition is false.
     *
     * @param message the identifying message for this assumption
     * @param condition the condition to evaluate
     */
    public static void assumeTrue(String message, boolean condition) {
        assumeThat(message, condition, is(true));
    }

    /**
     * Fails a test if the given value does not match the given matcher.
     *
     * @param value the actual value
     * @param matcher the matcher to apply to the actual value
     *
     * @see #assumeTrue(boolean)
     */
    public static <T> void assumeThat(T value, org.hamcrest.Matcher<T> matcher) {
        assumeThat(value, matcher, "");
    }

    /**
     * Fails a test if the given value does not match the given matcher.
     *
     * @param message the identifying message for this assumption
     * @param value the actual value
     * @param matcher the matcher to apply to the actual value
     */
    public static <T> void assumeThat(String message, T value, org.hamcrest.Matcher<T> matcher) {
        try {
            org.hamcrest.MatcherAssert.assertThat(message, value, matcher);
        } catch (org.hamcrest.AssertionError e) {
            throw new AssumptionViolatedException(e.getMessage());
        }
    }

    /**
     * Fails a test if the given condition is false.
     *
     * @param condition the condition to evaluate
     *
     * @see #assumeThat(boolean, String, org.hamcrest.Matcher)
     */
    public static void assumeFalse(boolean condition) {
        assumeThat(condition, is(false), "expected: false but was: true");
    }

    /**
     * Fails a test if the given condition is false.
     *
     * @param message the identifying message for this assumption
     * @param condition the condition to evaluate
     */
    public static void assumeFalse(String message, boolean condition) {
        assumeThat(message, condition, is(false));
    }

    /**
     * Fails a test if the given object is null.
     *
     * @param object the object to check
     */
    public static void assumeNotNull(Object object) {
        assumeNotNull(null, object);
    }

    /**
     * Fails a test if the given object is null.
     *
     * @param message the identifying message for this assumption
     * @param object the object to check
     */
    public static void assumeNotNull(String message, Object object) {
        assumeThat(message, object, org.hamcrest.Matchers.notNullValue());
    }

    /**
     * Fails a test if the given exception is not thrown.
     *
     * @param throwableClass the expected type of the exception
     * @param runnable the code expected to throw the exception
     *
     * @throws AssertionError if the given code does not throw an exception
     * @throws AssertionError if the given code throws an exception of the wrong type
     */
    public static void assumeNoException(Class<? extends Throwable> throwableClass, Runnable runnable) {
        try {
            runnable.run();
        } catch (Throwable e) {
            Class<?> exceptionClass = e.getClass();
            if (exceptionClass.equals(throwableClass)) {
                return;
            }
            String mismatchMessage = String.format(
                    "expected:<%s> but was:<%s>", throwableClass.getName(), exceptionClass.getName());
            fail(mismatchMessage);
        }
        fail(String.format("expected exception <%s> to be thrown, but nothing was thrown.",
                throwableClass.getName()));
    }

    /**
     * Fails a test if the current environment is not {@linkplain #isSupported() supported}.
     * This method can be invoked by test frameworks or test authors to detect if the
     * current environment is known to be unsuitable for running the test.
     *
     * <p>If a test framework detects that the current environment is
     * {@linkplain #isSupported() unsupported}, it should not run tests.
     *
     * <p>Test authors can invoke this method in their tests to skip them if the current
     * environment is not supported.
     *
     * <p>This mechanism is intended to allow tests to be written without needing to know
     * about all of the possible environments in which they might be run.
     *
     * <p>For example, a test that uses a particular operating system feature might invoke
     * {@code assumeTrue(Assume.isSupported())} to skip itself if it is run on an operating
     * system that does not support that feature.
     *
     * @since 5.3
     * @see #isSupported()
     */
    public static void assumeSupported() {
        assumeTrue("Test framework does not support the current environment", isSupported());
    }

    /**
     * Returns {@code true} if the current environment is supported, or {@code false} otherwise.
     * This method is intended to be invoked by test frameworks to determine whether the current
     * environment is suitable for running tests.
     *
     * <p>The default implementation of this method returns {@code true}.
     *
     * <p>Test frameworks that wish to support a subset of environments should override this
     * method to return {@code true} only for those environments.
     *
     * @since 5.3
     * @see #assumeSupported()
     */
    public static boolean isSupported() {
        return true;
    }
    
    public static <T> T[] copyOfRange(T[] original, int from, int to) {
        return copyOfRange(original, from, to, original.getClass());
    }
    @SuppressWarnings("unchecked")
    private static <T,U> T[] copyOfRange(U[] original, int from, int to, Class<? extends T[]> newType) {
        int newLength = to - from;
        if (newLength < 0)
            throw new IllegalArgumentException(from + " > " + to);
        T[] copy = ((Object)newType == (Object)Object[].class)
            ? (T[]) new Object[newLength]
            : (T[]) java.lang.reflect.Array.newInstance(newType.getComponentType(), newLength);
        arraycopy(original, from, copy, 0,
                 Math.min(original.length - from, newLength));
        return copy;
    }

    /**
     * Converts the given assumption to an {@link org.junit.Assumption}.
     *
     * <p>This method is called by the {@link org.junit.rules.TestWatcher}
     * when an assumption is violated.
     *
     * <p>The default implementation of this method returns a new
     * {@link org.junit.AssumptionViolatedException}.
     *
     * <p>Subclasses may override this method to provide alternative handling
     * of assumption violations. For example, a subclass might log the
     * assumption violation or send a notification to a remote server.
     *
     * @param assumption the assumption that was violated
     * @return an {@link org.junit.Assumption} object representing the violated assumption
     * @since 4.0
     */
    protected Assumption toAssumption(boolean assumption, String message) {
        return new Assumption(assumption, message);
    }

    /**
     * Handles the given assumption violation.
     *
     * <p>This method is called by the {@link org.junit.rules.TestWatcher}
     * when an assumption is violated.
     *
     * <p>The default implementation of this method throws a new
     * {@link org.junit.AssumptionViolatedException}.
     *
     * <p>Subclasses may override this method to provide alternative handling
     * of assumption violations. For example, a subclass might log the
     * assumption violation or send a notification to a remote server.
     *
     * @param e the assumption violation exception
     * @since 4.0
     */
    protected void handleAssumptionViolated(AssumptionViolatedException e) {
        throw e;
    }

    /**
     * An assumption that has been violated.
     *
     * @since 4.0
     */
    public static class AssumptionViolatedException extends RuntimeException {
        private static final long serialVersionUID = 1L;

        private final boolean fValue;

        /**
         * Creates a new assumption violation exception with the given message.
         *
         * @param message the identifying message for the assumption violation
         */
        public AssumptionViolatedException(String message) {
            this(message, true);
        }

        /**
         * Creates a new assumption violation exception with the given message
         * and value.
         *
         * @param message the identifying message for the assumption violation
         * @param value the value of the assumption
         * @since 4.13
         */
        public AssumptionViolatedException(String message, boolean value) {
            super(message);
            fValue = value;
        }

        /**
         * Returns the value of the assumption.
         *
         * @return the value of the assumption
         * @since 4.13
         */
        public boolean getValue() {
            return fValue;
        }
    }

    /**
     * An assumption that can be made about the current environment.
     *
     * @since 4.0
     */
    public static class Assumption {
        private final boolean fValue;
        private final String fMessage;

        private Assumption(boolean value, String message) {
            fValue = value;
            fMessage = message;
        }

        /**
         * Returns {@code true} if the assumption holds, and {@code false}
         * otherwise.
         *
         * @return {@code true} if the assumption holds, and {@code false}
         *         otherwise
         */
        public boolean isSatisfied() {
            return fValue;
        }

        /**
         * Returns the identifying message for this assumption.
         *
         * @return the identifying message for this assumption
         */
        public String getMessage() {
            return fMessage;
        }
    }
}
```