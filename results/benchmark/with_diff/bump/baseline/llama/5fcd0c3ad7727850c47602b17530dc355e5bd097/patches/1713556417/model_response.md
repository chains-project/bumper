Here's a possible patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass());
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
This patch creates a new `ClassInfoBuilder` instance and uses it to build a new `ClassInfo` instance for the mutated class. The `ClassInfo` instance is then passed to the `MutationTestSummaryData` constructor instead of the `CoverageDatabase` instance.

This patch works because the `CoverageDatabase` instance no longer has a `getClassInfo()` method, but the `ClassInfoBuilder` instance has a `build()` method that can be used to create a `ClassInfo` instance for a given class.

Note that this patch assumes that the `ClassMutationResults` instance passed to the `createSummaryData()` method contains the necessary information to build a `ClassInfo` instance for the mutated class. If this is not the case, additional changes may be needed to the patch.