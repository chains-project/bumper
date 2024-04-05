Here is a potential patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the call to `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()))` with `coverage.getClassInfoFor(data.getMutatedClass())`, which should achieve the same functionality but avoids the `cannot find symbol` error.

Note that I cannot be certain that this patch will fix the error without more context about the specific libraries and versions being used, but it should at least be a step in the right direction.