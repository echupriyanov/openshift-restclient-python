# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .v1_allowed_flex_volume import V1AllowedFlexVolume
from .v1_applied_cluster_resource_quota import V1AppliedClusterResourceQuota
from .v1_applied_cluster_resource_quota_list import V1AppliedClusterResourceQuotaList
from .v1_binary_build_source import V1BinaryBuildSource
from .v1_bitbucket_web_hook_cause import V1BitbucketWebHookCause
from .v1_broker_template_instance import V1BrokerTemplateInstance
from .v1_broker_template_instance_list import V1BrokerTemplateInstanceList
from .v1_broker_template_instance_spec import V1BrokerTemplateInstanceSpec
from .v1_build import V1Build
from .v1_build_config import V1BuildConfig
from .v1_build_config_list import V1BuildConfigList
from .v1_build_config_spec import V1BuildConfigSpec
from .v1_build_config_status import V1BuildConfigStatus
from .v1_build_list import V1BuildList
from .v1_build_log import V1BuildLog
from .v1_build_output import V1BuildOutput
from .v1_build_post_commit_spec import V1BuildPostCommitSpec
from .v1_build_request import V1BuildRequest
from .v1_build_source import V1BuildSource
from .v1_build_spec import V1BuildSpec
from .v1_build_status import V1BuildStatus
from .v1_build_status_output import V1BuildStatusOutput
from .v1_build_status_output_to import V1BuildStatusOutputTo
from .v1_build_strategy import V1BuildStrategy
from .v1_build_trigger_cause import V1BuildTriggerCause
from .v1_build_trigger_policy import V1BuildTriggerPolicy
from .v1_cluster_network import V1ClusterNetwork
from .v1_cluster_network_entry import V1ClusterNetworkEntry
from .v1_cluster_network_list import V1ClusterNetworkList
from .v1_cluster_resource_quota import V1ClusterResourceQuota
from .v1_cluster_resource_quota_list import V1ClusterResourceQuotaList
from .v1_cluster_resource_quota_selector import V1ClusterResourceQuotaSelector
from .v1_cluster_resource_quota_spec import V1ClusterResourceQuotaSpec
from .v1_cluster_resource_quota_status import V1ClusterResourceQuotaStatus
from .v1_cluster_role import V1ClusterRole
from .v1_cluster_role_binding import V1ClusterRoleBinding
from .v1_cluster_role_binding_list import V1ClusterRoleBindingList
from .v1_cluster_role_list import V1ClusterRoleList
from .v1_cluster_role_scope_restriction import V1ClusterRoleScopeRestriction
from .v1_custom_build_strategy import V1CustomBuildStrategy
from .v1_custom_deployment_strategy_params import V1CustomDeploymentStrategyParams
from .v1_deployment_cause import V1DeploymentCause
from .v1_deployment_cause_image_trigger import V1DeploymentCauseImageTrigger
from .v1_deployment_condition import V1DeploymentCondition
from .v1_deployment_config import V1DeploymentConfig
from .v1_deployment_config_list import V1DeploymentConfigList
from .v1_deployment_config_rollback import V1DeploymentConfigRollback
from .v1_deployment_config_rollback_spec import V1DeploymentConfigRollbackSpec
from .v1_deployment_config_spec import V1DeploymentConfigSpec
from .v1_deployment_config_status import V1DeploymentConfigStatus
from .v1_deployment_details import V1DeploymentDetails
from .v1_deployment_log import V1DeploymentLog
from .v1_deployment_request import V1DeploymentRequest
from .v1_deployment_strategy import V1DeploymentStrategy
from .v1_deployment_trigger_image_change_params import V1DeploymentTriggerImageChangeParams
from .v1_deployment_trigger_policy import V1DeploymentTriggerPolicy
from .v1_docker_build_strategy import V1DockerBuildStrategy
from .v1_docker_strategy_options import V1DockerStrategyOptions
from .v1_egress_network_policy import V1EgressNetworkPolicy
from .v1_egress_network_policy_list import V1EgressNetworkPolicyList
from .v1_egress_network_policy_peer import V1EgressNetworkPolicyPeer
from .v1_egress_network_policy_rule import V1EgressNetworkPolicyRule
from .v1_egress_network_policy_spec import V1EgressNetworkPolicySpec
from .v1_exec_new_pod_hook import V1ExecNewPodHook
from .v1_fs_group_strategy_options import V1FSGroupStrategyOptions
from .v1_generic_web_hook_cause import V1GenericWebHookCause
from .v1_git_build_source import V1GitBuildSource
from .v1_git_hub_web_hook_cause import V1GitHubWebHookCause
from .v1_git_lab_web_hook_cause import V1GitLabWebHookCause
from .v1_git_source_revision import V1GitSourceRevision
from .v1_group import V1Group
from .v1_group_list import V1GroupList
from .v1_group_restriction import V1GroupRestriction
from .v1_host_subnet import V1HostSubnet
from .v1_host_subnet_list import V1HostSubnetList
from .v1_id_range import V1IDRange
from .v1_identity import V1Identity
from .v1_identity_list import V1IdentityList
from .v1_image import V1Image
from .v1_image_change_cause import V1ImageChangeCause
from .v1_image_change_trigger import V1ImageChangeTrigger
from .v1_image_import_spec import V1ImageImportSpec
from .v1_image_import_status import V1ImageImportStatus
from .v1_image_label import V1ImageLabel
from .v1_image_layer import V1ImageLayer
from .v1_image_list import V1ImageList
from .v1_image_lookup_policy import V1ImageLookupPolicy
from .v1_image_signature import V1ImageSignature
from .v1_image_source import V1ImageSource
from .v1_image_source_path import V1ImageSourcePath
from .v1_image_stream import V1ImageStream
from .v1_image_stream_image import V1ImageStreamImage
from .v1_image_stream_import import V1ImageStreamImport
from .v1_image_stream_import_spec import V1ImageStreamImportSpec
from .v1_image_stream_import_status import V1ImageStreamImportStatus
from .v1_image_stream_list import V1ImageStreamList
from .v1_image_stream_mapping import V1ImageStreamMapping
from .v1_image_stream_spec import V1ImageStreamSpec
from .v1_image_stream_status import V1ImageStreamStatus
from .v1_image_stream_tag import V1ImageStreamTag
from .v1_image_stream_tag_list import V1ImageStreamTagList
from .v1_jenkins_pipeline_build_strategy import V1JenkinsPipelineBuildStrategy
from .v1_lifecycle_hook import V1LifecycleHook
from .v1_local_resource_access_review import V1LocalResourceAccessReview
from .v1_named_tag_event_list import V1NamedTagEventList
from .v1_net_namespace import V1NetNamespace
from .v1_net_namespace_list import V1NetNamespaceList
from .v1_o_auth_access_token import V1OAuthAccessToken
from .v1_o_auth_access_token_list import V1OAuthAccessTokenList
from .v1_o_auth_authorize_token import V1OAuthAuthorizeToken
from .v1_o_auth_authorize_token_list import V1OAuthAuthorizeTokenList
from .v1_o_auth_client import V1OAuthClient
from .v1_o_auth_client_authorization import V1OAuthClientAuthorization
from .v1_o_auth_client_authorization_list import V1OAuthClientAuthorizationList
from .v1_o_auth_client_list import V1OAuthClientList
from .v1_parameter import V1Parameter
from .v1_pod_security_policy_review import V1PodSecurityPolicyReview
from .v1_pod_security_policy_review_spec import V1PodSecurityPolicyReviewSpec
from .v1_pod_security_policy_review_status import V1PodSecurityPolicyReviewStatus
from .v1_pod_security_policy_self_subject_review import V1PodSecurityPolicySelfSubjectReview
from .v1_pod_security_policy_self_subject_review_spec import V1PodSecurityPolicySelfSubjectReviewSpec
from .v1_pod_security_policy_subject_review import V1PodSecurityPolicySubjectReview
from .v1_pod_security_policy_subject_review_spec import V1PodSecurityPolicySubjectReviewSpec
from .v1_pod_security_policy_subject_review_status import V1PodSecurityPolicySubjectReviewStatus
from .v1_policy_rule import V1PolicyRule
from .v1_project import V1Project
from .v1_project_list import V1ProjectList
from .v1_project_request import V1ProjectRequest
from .v1_project_spec import V1ProjectSpec
from .v1_project_status import V1ProjectStatus
from .v1_recreate_deployment_strategy_params import V1RecreateDeploymentStrategyParams
from .v1_repository_import_spec import V1RepositoryImportSpec
from .v1_repository_import_status import V1RepositoryImportStatus
from .v1_resource_access_review import V1ResourceAccessReview
from .v1_resource_quota_status_by_namespace import V1ResourceQuotaStatusByNamespace
from .v1_role import V1Role
from .v1_role_binding import V1RoleBinding
from .v1_role_binding_list import V1RoleBindingList
from .v1_role_binding_restriction import V1RoleBindingRestriction
from .v1_role_binding_restriction_list import V1RoleBindingRestrictionList
from .v1_role_binding_restriction_spec import V1RoleBindingRestrictionSpec
from .v1_role_list import V1RoleList
from .v1_rolling_deployment_strategy_params import V1RollingDeploymentStrategyParams
from .v1_route import V1Route
from .v1_route_ingress import V1RouteIngress
from .v1_route_ingress_condition import V1RouteIngressCondition
from .v1_route_list import V1RouteList
from .v1_route_port import V1RoutePort
from .v1_route_spec import V1RouteSpec
from .v1_route_status import V1RouteStatus
from .v1_route_target_reference import V1RouteTargetReference
from .v1_run_as_user_strategy_options import V1RunAsUserStrategyOptions
from .v1_se_linux_context_strategy_options import V1SELinuxContextStrategyOptions
from .v1_scope_restriction import V1ScopeRestriction
from .v1_secret_build_source import V1SecretBuildSource
from .v1_secret_spec import V1SecretSpec
from .v1_security_context_constraints import V1SecurityContextConstraints
from .v1_security_context_constraints_list import V1SecurityContextConstraintsList
from .v1_self_subject_rules_review import V1SelfSubjectRulesReview
from .v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from .v1_service_account_pod_security_policy_review_status import V1ServiceAccountPodSecurityPolicyReviewStatus
from .v1_service_account_reference import V1ServiceAccountReference
from .v1_service_account_restriction import V1ServiceAccountRestriction
from .v1_signature_condition import V1SignatureCondition
from .v1_signature_issuer import V1SignatureIssuer
from .v1_signature_subject import V1SignatureSubject
from .v1_source_build_strategy import V1SourceBuildStrategy
from .v1_source_control_user import V1SourceControlUser
from .v1_source_revision import V1SourceRevision
from .v1_source_strategy_options import V1SourceStrategyOptions
from .v1_stage_info import V1StageInfo
from .v1_step_info import V1StepInfo
from .v1_subject_rules_review import V1SubjectRulesReview
from .v1_subject_rules_review_spec import V1SubjectRulesReviewSpec
from .v1_subject_rules_review_status import V1SubjectRulesReviewStatus
from .v1_supplemental_groups_strategy_options import V1SupplementalGroupsStrategyOptions
from .v1_tls_config import V1TLSConfig
from .v1_tag_event import V1TagEvent
from .v1_tag_event_condition import V1TagEventCondition
from .v1_tag_image_hook import V1TagImageHook
from .v1_tag_import_policy import V1TagImportPolicy
from .v1_tag_reference import V1TagReference
from .v1_tag_reference_policy import V1TagReferencePolicy
from .v1_template import V1Template
from .v1_template_instance import V1TemplateInstance
from .v1_template_instance_condition import V1TemplateInstanceCondition
from .v1_template_instance_list import V1TemplateInstanceList
from .v1_template_instance_object import V1TemplateInstanceObject
from .v1_template_instance_requester import V1TemplateInstanceRequester
from .v1_template_instance_spec import V1TemplateInstanceSpec
from .v1_template_instance_status import V1TemplateInstanceStatus
from .v1_template_list import V1TemplateList
from .v1_user import V1User
from .v1_user_identity_mapping import V1UserIdentityMapping
from .v1_user_list import V1UserList
from .v1_user_restriction import V1UserRestriction
from .v1_web_hook_trigger import V1WebHookTrigger
from .v1beta1_ingress_tls import V1beta1IngressTLS