Here's the proposed patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
The change in the code is to replace `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()))` with `coverage.getClassInfoFor(data.getMutatedClass())`.

The method `getClassInfoFor` was added in a newer version of pitest-coverage library, as a replacement for the removed `getClassInfo` method that takes a Set of ClassName.

The `getClassInfoFor` method is available in pitest-coverage version 1.5.0 or higher.

If the version of pitest-coverage used is lower than 1.5.0, you may need to update the library to a higher version.