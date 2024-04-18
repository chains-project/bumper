Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoBuilder().getClassInfo(data.getMutatedClass()));
}
```
The patch replaces the line `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));` with `coverage.getClassInfoBuilder().getClassInfo(data.getMutatedClass());`, which uses the added method `getClassInfoBuilder()` to retrieve a `ClassInfo` object for the mutated class.

Note that this patch assumes that the `getClassInfoBuilder()` method returns a `ClassInfoBuilder` instance that can be used to retrieve the `ClassInfo` object for the mutated class. If this is not the case, additional changes may be necessary to the patch.