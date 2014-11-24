----------- Shankar code begin-------------------

create table pid (
	set_id_pid 				integer unique,
	patient_identifier_list 		varchar(256),
	alternate_patient_id 			integer,
	patient_name 				varchar(128),
	mothers_maiden_name 			varchar(128),
	date_time_of_birth 			timestamp,
	administrative_sex 			varchar(6),
	patient_alias 				varchar(128),
	race 					varchar(64),
	patient_address 			varchar(256),
	country_code 				varchar(3),
	phone_number_home 			varchar(32),
	phone_number_business 			varchar(32),
	primary_language 			varchar(32),
	martial_status 				varchar(16),
	religion 				varchar(32),
	patient_account_number 			integer,
	ssn_number_patient 			varchar(11),
	drivers_license_number_patient 		varchar(32),
	mothers_identifier 			varchar(16),
	ethnic_group 				varchar(16),
	birth_place 				varchar(64),
	multiple_birth_indicator 		boolean,
	birth_order 				integer,
	citizenship 				varchar(32),
	veteran_military_status 		varchar(16),
	nationality 				varchar(32),
	patient_death_date_time 		timestamp,
	patient_death_indicator  		boolean,
	identity_unknown_indicator 		boolean,
	identity_reliability_code 		integer,
	last_update_date_time 			timestamp,
	last_update_facility 			varchar(64),
	species_code 				varchar(64),
	breed_code 				varchar(64),
	strain 					varchar(64),
	production_class_code  			varchar(32),
	tribal_citizenship 			varchar(64),
patient_id 				integer primary key
);

create table abs (
	discharge_care_provider			varchar(250),
	transfer_medical_service_code		varchar(250),
	severity_of_illness_code		varchar(250),
	date_time_of_attestation		timestamp,
	attested_by				varchar(250),
	triage_code				varchar(250),
	abstract_completed_date_time		timestamp,
	abstract_by				varchar(250),
	case_category_code			varchar(250),
	caesarian_section_indicator		boolean,
	gestation_category_code			varchar(250),
	gestation_period_weeks			integer,
	newborn_code				varchar(250),
	stillborn_indicator			boolean,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table acc (
	accident_date_time			timestamp,
	accident_code				varchar(250),
	accident_location			varchar(25),
	auto_accident_state			varchar(2),
	accident_job_related_indicator		boolean,
	accident_death_indicator		varchar(12),
	entered_by				varchar(3220),
	accident_description			varchar(25),
	brought_in_by				varchar(80),
	police_notified_indicator		boolean,
	accident_address			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table add (
	addendum_continuation_pointer		long varchar(655360),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table adj (
	provider_adjustment_number		varchar(73),
	payer_adjustment_number			varchar(73),
	adjustment_sequence_number		varchar(4),
	adjustment_category			varchar(4),
	adjustment_amount			varchar(254),
	adjustment_quantity			varchar(222),
	adjustment_reason_pa			varchar(211),
	adjustment_description			varchar(250),
	original_value				varchar(250),
	substitute_value			varchar(250),
	adjustment_action			varchar(4),
	provider_adjustment_number_cross_reference varchar(73),
	provider_product_service_line_item_number_cross_reference varchar(73),
	adjustment_date				timestamp,
	responsible_organization		varchar(183),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table aff (
	set_id_aff					integer primary key,
	professional_organization			varchar(250),
	professional_organization_address		varchar(250),
	professional_organization_affiliation_date_range varchar(250),
	professional_affiliation_additional_information	varchar(60),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table aig (
	set_id_aig				integer primary key,
	segment_action_code			varchar(3),
	resource_id				varchar(250),
	resource_type				varchar(250),
	resource_group				varchar(250),
	resource_quantity			varchar(5),
	resource_quantity_units			varchar(250),
	start_date_time				varchar(24),
	start_date_time_offset			varchar(20),
	start_date_time_offset_units		varchar(250),
	duration				varchar(20),
	duration_units				varchar(250),
	allow_substitution_code			varchar(10),
	filler_status_code			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table ail (
	set_id_ail				varchar(4),
	segment_action_code			varchar(3),
	location_resource_id			varchar(80),
	location_type_ail			varchar(250),
	location_group				varchar(250),
	start_date_time				varchar(24),
	start_date_time_offset			varchar(20),
	start_date_time_offset_units		varchar(250),
	duration				varchar(20),
	duration_units				varchar(250),
	allow_substitution_code			varchar(10),
	filler_status_code			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table aip (
	set_id_aip				varchar(4),
	segment_action_code			varchar(3),
	personnel_resource_id			varchar(250),
	resource_type				varchar(250),
	resource_group				varchar(250),
	start_date_time				varchar(24),
	start_date_time_offset			varchar(20),
	start_date_time_offset_units		varchar(250),
	duration				varchar(20),
	duration_units				varchar(250),
	allow_substitution_code			varchar(10),
	filler_status_code			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table ais (
	set_id_ais				varchar(4),
	segment_action_code			varchar(3),
	universal_service_identifier		varchar(750),
	start_date_time				varchar(24),
	start_date_time_offset			varchar(20),
	start_date_time_offset_units		varchar(250),
	duration				varchar(20),
	duration_units				varchar(250),
	allow_substitution_code			varchar(10),
	filler_status_code			varchar(250),
	placer_supplemental_service_info	varchar(750),
	filler_supplemental_service_info	varchar(750),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table al1 (
	set_id_al1				integer primary key,
	allergen_type_code			varchar(16),
	allergen_code				varchar(16),
	allergy_severity_code			varchar(16),
	allergy_reaction_code			varchar(16),
	identification_date			timestamp,

	patient_id				integer,

	foreign key (patient_id) references pid (patient_id)
);

create table apr (
	time_selection_criteria			varchar(80),
	resource_selection_criteria		varchar(80),
	location_selection_criteria		varchar(80),
	slot_spacing_criteria			varchar(5),
	filler_override_criteria		varchar(80),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table arq  (
	placer_appointment_id			varchar(75),
	filler_appointment_id			varchar(75),
	occurrence_number			varchar(5),
	placer_group_number			varchar(22),
	schedule_id				varchar(250),
	request_event_reason			varchar(250),
	appointment_reason			varchar(250),
	appointment_type			varchar(250),
	appointment_duration			integer,
	appointment_duration_units		varchar(40),
	requested_start_date_time_range		varchar(49),
	priority_arq				varchar(5),
	rerpeating_interval			varchar(100),
	repeating_interval_duration		varchar(5),
	placer_contact_person			varchar(250),
	placer_contact_phone_number		varchar(250),
	placer_contact_address			varchar(250),
	placer_contact_location			varchar(80),
	entered_by_person			varchar(250),
	entered_by_phone_number			varchar(250),
	entered_by_location			varchar(80),
	parent_placer_appointment_id		varchar(75),
	parent_filler_appointment_id		varchar(75),
	placer_order_number			varchar(427),
	filler_order_number			varchar(427),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table arv (
	set_id					varchar(4),
	access_restriction_action_code		varchar(750),
	access_restriction_value		varchar(705),
	access_restriction_reason		varchar(705),
	special_access_restriction_instructions varchar(250),
	access_restriction_date_range		varchar(49),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table aut (
	authorizing_payor_plan_id		varchar(250),
	authorizing_payor_company_id		varchar(250),
	authorizing_payor_company_name		varchar(45),
	authorization_effective_date		timestamp,
	authorization_expiration_date		timestamp,
	authorization_identifier		varchar(30),
	reimbursement_limit			varchar(25),
	requested_number_of_treatments		integer,
	authorized_number_of_treatments		integer,
	process_date				timestamp,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table bhs (
	batch_field_separator			boolean,
	batch_encoding_characters		varchar(4),
	batch_sending_application		varchar(227),
	batch_sending_facility			varchar(227),
	batch_receiving_application		varchar(227),
	batch_receiving_facility		varchar(227),
	batch_creation_date_time		timestamp,
	batch_security				varchar(40),
	batch_name_type_id			varchar(20),
	batch_comment				varchar(80),
	batch_control_id			varchar(20),
	reference_batch_control_id		varchar(20),
	batch_sending_network_address		varchar(227),
	batch_receiving_network_address		varchar(227),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table blc (
	blood_product_code			varchar(250),
	blood_amount				varchar(267),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table blg (
	when_to_charge				varchar(40),
	charge_type				varchar(50),
	account_id				varchar(100),
	charge_type_reason			varchar(60),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table bpo (
	set_id_bpo				integer primary key,
	bp_universal_service_identifier		varchar(250),
	bp_processing_requirements		varchar(250),
	bp_quantity				integer,
	bp_amount				integer,
	bp_units				varchar(250),
	bp_intended_use_date_time		timestamp,
	bp_intended_dispense_from_location	varchar(80),
	bp_intended_dispense_from_address	varchar(250),
	bp_requested_dispense_date_time		timestamp,
	bp_requested_dispense_to_location	varchar(80),
	bp_requested_dispense_to_address	varchar(250),
	bp_indication_for_use			varchar(250),
	bp_informed_consent_indicator		boolean,
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table bpx (
	set_id_bpx				integer primary key,
	bp_dispense_status			varchar(250),
	bp_status				varchar(1),
	bp_date_time_of_status			timestamp,
	bc_donation_id				varchar(22),
	bc_component				varchar(250),
	bc_donation_type_intended_use		varchar(250),
	cp_commercial_product			varchar(250),
	cp_manufacturer				varchar(250),
	cp_lot_number				varchar(22),
	bp_blood_group				varchar(250),
	bc_special_testing			varchar(250),
	bp_expiration_date_time			timestamp,
	bp_quantity				integer,
	bp_amount				integer,
	bp_units				varchar(250),
	bp_unique_id				varchar(22),	
	bp_actual_dispensed_to_address		varchar(250),
	bp_actual_dispensed_to_location		varchar(80),
	bp_dispensed_to_receiver		varchar(250),
	bp_dispensing_individual		varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table bts (
	batch_message_count			varchar(10),
	batch_comment				varchar(80),
	batch_totals				varchar(100),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);


create table btx (
	set_id_btx				varchar(4),
	bc_donation_id				varchar(22),
	bc_component				varchar(250),
	bc_blood_group				varchar(250),
	cp_commercial_product			varchar(250),
	cp_manufacturer				varchar(250),
	cp_lot_number				varchar(22),
	bp_quantity				integer,
	bp_amount				integer,
	bp_units				varchar(250),
	bp_transfusion_disposition_status	varchar(250),
	bp_message_status			varchar(1),
	bp_date_time_of_status			timestamp,
	bp_transfusion_administrator		varchar(250),
	bp_transfusion_verifier			varchar(250),
	bp_transfusion_start_date_time_of_status timestamp,
	bp_transfusion_end_date_time_of_status	timestamp,
	bp_adverse_reaction_type		varchar(250),
	bp_transfusion_interrupted_reason	varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cdm (
	primary_key_value_cdm			varchar(250),
	charge_code_alias			varchar(250),
	charge_description_short		varchar(20),
	charge_description_long			varchar(250),
	description_override_indicator		boolean,
	exploding_charges			varchar(250),
	procedure_code				varchar(705),
	active_inactive_flag			boolean,
	inventory_number			varchar(250),
	resource_load				varchar(12),
	contract_number				varchar(250),
	contract_organization			varchar(250),
	room_fee_indicator			boolean,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cer (
	set_id_cer				varchar(4),
	serial_number				varchar(80),
	version					varchar(80),
	granting_authority			varchar(250),
	issuing_authority			varchar(250),
	signature_involving_issuing_authority	long varchar(65536),
	granting_country			varchar(3),
	granting_state_province			varchar(250),
	granting_county_parish			varchar(250),
	certificate_type			varchar(250),
	certificate_domain			varchar(250),
	subject_id				varchar(250),
	subject_name				varchar(250),
	subject_directory_attribute_expression	varchar(250),
	subject_public_key_info			varchar(250),
	authority_key_identifier		varchar(250),
	basic_constraint			varchar(250),
	crl_distribution_point			varchar(250),
	jurisdiction_country			varchar(3),
	jurisdiction_state_province		varchar(250),
	jurisdiction_county_parish		varchar(250),
	jurisdiction_breadth			varchar(250),
	granting_date				timestamp,
	issuing_date				timestamp,
	activation_date				timestamp,
	inactivation_date			timestamp,
	expiration_date				timestamp,
	renewal_date				timestamp,
	revocation_date				timestamp,
	revocation_reason_code			varchar(250),
	certificate_status_code			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cm0 (
	set_id_cm0 				integer primary key,
	sponsor_study_id			varchar(427),
	alternate_study_id			varchar(427),
	title_of_study				varchar(300),
	chairman_of_study			varchar(250),
	last_irb_approval_date			varchar(8),
	total_accrual_to_date			varchar(8),
	last_accrual_date			timestamp,
	contact_for_study			varchar(250),
	contacts_telephone_number		varchar(250),
	contacts_adadress			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cm1 (
	set_id_cm1				varchar(4),
	study_phase_identifier			varchar(705),
	description_of_study_phase		varchar(300),


	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cm2 (
	set_id_cm2				varchar(4),
	scheduled_time_point			varchar(250),
	description_of_time_point		varchar(300),
	events_scheduled_this_time_point	varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cns (
	starting_notification_reference_number	varchar(20),
	ending_notification_reference_number	varchar(20),
	starting_notification_date_time		timestamp,
	ending_notification_date_time		timestamp,
	starting_notification_code		varchar(705),
	ending_notification_code		varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table con (
	set_id_con				varchar(4),
	consent_type				varchar(705),
	consent_form_id_and_version		varchar(40),
	consent_form_number			varchar(427),
	consent_text				long varchar(65536),
	subject_specific_consent_text		long varchar(65536),
	consent_background_information		long varchar(65536),
	subject_specific_consent_background_text long varchar(65536),
	consenter_imposed_limitations		long varchar(65536),
	consent_mode				varchar(2),
	consent_status				varchar(2),
	consent_discussion_date_time		timestamp,
	consent_decision_date_time		timestamp,
	consent_effective_date_time		timestamp,
	consent_end_date_time			timestamp,
	subject_competence_indicator		boolean,
	translator_assistance_indicator		boolean,
	language_translated_to			varchar(250),
	informational_material_supplied_indicator boolean,
	consent_bypass_reason			varchar(705),
	consent_disclosure_level		integer,
	consent_non_disclosure_reason		varchar(705),
	non_subject_consenter_reason		varchar(705),
	consenter_id				varchar(250),
	relationship_to_subject			varchar(100),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table csp (
	study_phase_identifier			varchar(705),
	date_time_study_phase_began		timestamp,
	date_time_study_phase_ended		timestamp,
	study_phase_evaluability		varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table csr (
	sponsor_study_id			varchar(427),
	alternate_study_id			varchar(427),
	institution_registering_the_patient	varchar(705),
	sponsor_patient_id			varchar(1913),
	alternate_patient_id_csr		varchar(1913),
	date_time_of_patient_study_registration	timestamp,
	person_performing_study_registration	varchar(3220),
	study_authorizing_provider		varchar(3220),
	date_time_patient_study_consent_signed	timestamp,
	patient_study_eligibility_status	varchar(705),
	study_randomization_date_time		timestamp,
	randomized_study_arm			varchar(705),
	stratum_for_study_randomization		varchar(705),
	patient_evaluability_status		varchar(705),
	date_time_ended_study			timestamp,
	reason_ended_study			varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table css (
	study_scheduled_time_point		varchar(705),
	study_scheduled_patient_time_point	timestamp,
	study_quality_control_codes		varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table ctd (
	contact_role				varchar(705),
	contact_name				varchar(250),
	contact_address				varchar(2915),
	contact_location			varchar(60),
	contact_communication_information	varchar(250),
	preferred_method_of_contact		varchar(705),
	contact_identifiers			varchar(100),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table cti (
	sponsor_study_id			varchar(427),
	study_phase_indicator			varchar(705),
	study_scheduled_time_point		varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table db1 (
	set_id_db1				integer primary key,
	disabled_person_code			varchar(2),
	disabled_person_identifier		varchar(250),
	disability_indicator			boolean,
	disablility_start_date			date,
	disability_end_date			date,
	disability_return_to_work_date		date,
	disability_unable_to_work_date		date,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table dg1 (
	set_id_dg1				integer primary key,
	diagnosis_coding_method			varchar(10),
	diagnosis_code_dg1			varchar(250),
	diagnosis_description			varchar(64),
	diagnosis_date_time			timestamp,
	diagnosis_type				varchar(2),
	major_diagnostic_category		varchar(1),
	diagnostic_related_group		varchar(250),
	drg_approval_indicator			varchar(1),
	drg_grouper_review_code			varchar(2),
	outlier_type				varchar(250),
	outlier_days				varchar(3),
	outlier_cost				varchar(12),
	grouper_version_and_type		varchar(10),
	diagnosis_priority			varchar(2),
	diagnosing_clinician			varchar(250),
	diagnosis_classification		varchar(3),
	confidential_indicator			boolean,
	attestation_date_time			timestamp,
	diagnosis_identifier			varchar(427),
	diagnosis_action_code			varchar(1),
	parent_diagnosis			varchar(427),	
	drg_ccl_value_code			varchar(705),
	drg_grouping_usage			varchar(20),
	drg_diagnosis_determination_status	varchar(20),
	present_on_admission_indicator		boolean,

	patient_id				integer,

	foreign key (patient_id) references pid (patient_id)
);

create table dmi (
	diagnostic_related_group		varchar(250),
	major_diagnostic_category		varchar(1),
	lower_and_upper_trim_points		varchar(7),
	average_length_of_stay			varchar(5),
	relative_weight				varchar(7),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table drg (
	diagnostic_related_group		varchar(250),
	drg_assigned_date_time			timestamp,
	drg_approval_indicator			boolean,
	drg_grouper_review_code			varchar(2),
	outlier_type				varchar(250),
	outlier_days				varchar(3),
	outlier_cost				varchar(12),
	drg_payor				varchar(1),
	outlier_reimbursement			varchar(9),
	confidential_indicator			boolean,
	drg_transfer_type			varchar(21),
	name_of_coder				varchar(1103),
	grouper_status				varchar(705),
	pccl_value_code				varchar(20),
	effective_weight			varchar(5),
	monetary_amount				varchar(20),
	status_patient				varchar(20),
	grouper_software_name			varchar(100),
	grouper_software_version		varchar(100),
	status_financial_calculation		varchar(20),
	relative_discount_surcharge		varchar(20),
	basic_charge				varchar(20),
	total_charge				varchar(20),
	discount_surcharge			varchar(20),
	calculated_days				varchar(5),
	status_gender				varchar(20),
	status_age				varchar(20),
	status_length_of_stay			varchar(20),
	status_same_day_flag			varchar(20),
	status_separation_mode			varchar(20),
	status_weight_at_birth			varchar(20),
	status_respiration_minutes		varchar(20),
	status_admission			varchar(20),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table dsc (
	continuation_pointer			varchar(180),
	continuation_style			varchar(1),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table dsp (
	set_id_dsp				integer primary key,
	display_level				varchar(4),
	data_line				varchar(300),
	logical_break_point			varchar(2),
	result_id				varchar(20),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table ecd (
	reference_command_number		varchar(20),
	remote_control_command			varchar(250),
	response_required			varchar(80),
	requested_completion_time		varchar(10),
	parameters				long varchar(65536),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table ecr (
	command_response			varchar(705),
	date_time_completed			timestamp,
	command_response_parameters		long varchar(65536),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table edu (
	set_id_edu				integer primary key,
	academic_degree				varchar(10),
	academic_degree_program_date_range	varchar(52),
	academic_degree_program_participation_date_range varchar(52),
	academic_degree_granted_date		timestamp,
	school					varchar(250),
	school_type_code			varchar(250),
	school_address				varchar(250),
	major_field_of_study			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table eqp (
	event_type				varchar(705),
	file_name				varchar(20),
	start_date_time				timestamp,
	end_date_time				timestamp,
	transaction_data			long varchar(65536),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table equ (
	equipment_instance_identifier		varchar(427),
	event_date_time				timestamp,
	equipment_state				varchar(705),
	local_remote_control_state		varchar(705),
	alert_level				varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table err (
	error_code_and_location			varchar(10),
	error_location				varchar(18),
	hl7_error_code				varchar(705),
	severity				varchar(2),
	application_error_code			varchar(705),
	application_error_parameter		varchar(80),
	diagnostic_information			varchar(2048),
	user_message				varchar(250),
	inform_person_indicator			varchar(20),
	override_type				varchar(705),
	override_reason_code			varchar(705),
	help_desk_contact_point			varchar(652),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table evn (
	event_type_code				varchar(10),
	recorded_date_time			timestamp,
	date_time_planned_event			timestamp,
	event_reason_code			varchar(3),
	operator_id				varchar(250),
	event_occurred				timestamp,
	event_facility				varchar(241),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table fac (
	facility_id_fac				varchar(427),
	facility_type				varchar(10),
	facility_address			varchar(2915),
	facility_telecommunication		varchar(2743),
	contact_person				varchar(3220),
	contact_title				varchar(60),
	contact_address				varchar(2915),
	contact_telecommunication		varchar(2743),
	signature_authority			varchar(3220),
	signature_authority_title		varchar(199),
	signature_authority_address		varchar(2915),
	signature_authority_telecommunication	varchar(2743),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table fhs (
	file_field_separator			varchar(1),
	file_encoding_characters		varchar(4),
	file_sending_application		varchar(227),
	file_sending_facility			varchar(227),
	file_receiving_application		varchar(227),
	file_receiving_facility			varchar(227),
	file_creation_date_time			timestamp,
	file_security				varchar(40),
	file_name_id				varchar(20),
	file_header_comment			varchar(80),
	file_control_id				varchar(20),
	reference_file_control_id		varchar(20),
	file_sending_network_address		varchar(227),
	file_receiving_network_address		varchar(227),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table ft1 (
	set_id_ft1				integer primary key,
	transaction_id				varchar(12),
	transaction_batch_id			varchar(10),
	transaction_date			varchar(53),
	transaction_posting_date		timestamp,
	transaction_type			varchar(8),
	transaction_code			varchar(250),
	transaction_description			varchar(250),
	transaction_description_alt		varchar(250),
	transaction_quantity			varchar(6),
	transaction_amount_extended		varchar(12),
	transaction_amount_unit			varchar(12),
	department_code				varchar(250),
	insurance_plan_id			varchar(250),
	insurance_amount			varchar(12),
	assigned_patient_location		varchar(80),
	fee_schedule				varchar(1),
	patient_type				varchar(2),
	diagnosis_code_ft1			varchar(250),
	performed_by_code			varchar(250),
	ordered_by_code				varchar(250),
	unit_cost				varchar(12),
	filler_order_number			varchar(427),
	entered_by_code				varchar(250),
	procedure_code				varchar(705),
	procedure_code_modifier			varchar(705),
	advanced_beneficiary_notice_code	varchar(250),
	medically_neceessary_duplicate_procedure_reason varchar(705),
	ndc_ccode				varchar(250),
	payment_reference_id			varchar(250),
	transaction_reference_key		varchar(4),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table fts (
	file_batch_count			varchar(10),
	file_trailer_comment			varchar(80),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table gol (
	action_code				varchar(2),
	action_date_time			timestamp,
	goal_id					varchar(705),
	goal_instance_id			varchar(60),
	episode_of_care_id			varchar(60),
	goal_list_priority			varchar(60),
	goal_established_date_time		timestamp,
	expected_goal_achieve_date_time		timestamp,
	goal_classification			varchar(705),
	goal_management_discipline		varchar(705),
	current_goal_review_status		varchar(705),
	current_goal_review_date_time		timestamp,
	next_goal_review_date_time		timestamp,
	previous_goal_review_date_time		timestamp,
	goal_review_interval			varchar(200),
	goal_evaluation				varchar(705),
	goal_evaluation_comment			varchar(300),
	goal_life_cycle_status			varchar(705),
	goal_life_cycle_status_date_time	timestamp,
	goal_target_type			varchar(705),
	goal_target_name			varchar(250),
	mood_code				varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table gp1 (
	type_of_bill_code			varchar(3),
	revenue_code				varchar(3),
	overall_claim_disposition_code		varchar(1),
	oce_edits_per_visit_code		varchar(2),
	outlier_cost				varchar(12),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table gp2 (
	revenue_code				varchar(3),
	number_of_service_units			varchar(7),
	charge					varchar(12),
	reimbursement_action_code		varchar(1),
	denial_or_rejection_code		varchar(1),
	oce_edit_code				varchar(3),
	ambulatory_payment_classification_code	varchar(250),
	modifier_edit_code			varchar(1),
	payment_adjustment_code			varchar(1),
	packaging_status_code			varchar(1),
	expected_cms_payment_amount		varchar(12),
	reimbursement_type_code			varchar(2),
	co_pay_amount				varchar(12),
	pay_rate_per_service_unit		varchar(4),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table gt1 (
	set_id_gt1				integer primary key,
	guarantor_number			varchar(250),
	guarantor_name				varchar(250),
	guarantor_spouse_name			varchar(250),
	guarantor_address			varchar(250),
	guarantor_ph_number_home		varchar(250),
	guarantor_ph_number_business		varchar(250),
	guarantor_date_time_of_birth		timestamp,
	guarantor_administrative_sex		varchar(1),
	guarantor_type				varchar(2),
	guarantor_relationship			varchar(250),
	guarantor_ssn				varchar(11),
	guarantor_date_begin			date,
	guarantor_date_end			date,
	guarantor_priority			varchar(2),
	guarantor_employer_name			varchar(250),
	guarantor_employer_address		varchar(250),
	guarantor_employer_phone_number		varchar(250),
	guarantor_employee_id_number		varchar(250),
	guarantor_employment_status		varchar(2),
	guarantor_organization_name		varchar(250),
	guarantor_billing_hold_flag		boolean,
	guarantor_credit_rating_code		varchar(250),
	guarantor_death_date_time		timestamp,
	guarantor_death_flag			boolean,
	guarantor_charge_adjustment_code	varchar(250),
	guarantor_household_annual_income	varchar(10),
	guarantor_household_size		varchar(3),
	guarantor_employer_id_number		varchar(250),
	guarantor_martial_status_code		varchar(250),
	guarantor_hire_effective_date		date,
	employment_stop_date			date,
	living_dependency			varchar(2),
	ambulatory_status			varchar(2),
	citizenship				varchar(705),
	primary_language			varchar(705),
	living_arrangement			varchar(2),
	publicity_code				varchar(705),
	protection_indicator			boolean,
	student_indicator			varchar(2),
	religion				varchar(705),
	mothers_maiden_name			varchar(250),
	nationality				varchar(10),
	ethnic_group				varchar(705),
	contact_persons_name			varchar(250),
	contact_persons_telephone_number	varchar(250),
	contact_reason				varchar(705),
	contact_relationship			varchar(3),
	job_title				varchar(20),
	job_code_class				varchar(20),
	guarantor_employers_organization_name	varchar(250),
	handicap				varchar(2),
	job_status				varchar(2),
	guarantor_financial_class		varchar(50),
	guarantor_race				varchar(250),
	guarantor_birth_place			varchar(250),
	vip_indicator				varchar(2),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table iam (
	set_id_iam				integer primary key,
	allergen_type_code			varchar(705),
	allergen_code_mnemonic_description	varchar(705),
	allergy_severity_code			varchar(705),
	allergy_reaction_code			varchar(15),
	allergy_action_code			varchar(250),
	allergy_unique_identifier		varchar(427),
	action_reason				varchar(60),
	sensitivity_to_causative_agent_code	varchar(705),
	allergen_group_code_mnemonic_description  varchar(705),
	onset_date				date,
	onset_date_text				varchar(80),
	reported_date_time			timestamp,
	reported_by				varchar(250),
	relationship_to_patient_code		varchar(705),
	alert_device_code			varchar(705),
	allergy_clinical_status_code		varchar(705),
	statused_by_person			varchar(250),
	statused_by_organization		varchar(250),
	statused_at_date_time			timestamp,


	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);

create table iim (
	primary_key_value_iim			varchar(250) primary key,
	service_item_code			varchar(250),
	inventory_lot_number			varchar(250),
	inventory_expiration_date		timestamp,
	inventory_manufacturer_name		varchar(250),
	inventory_location			varchar(250),
	inventory_received_date			timestamp,
	inventory_received_quantity		varchar(12),
	inventory_received_quantity_unit	varchar(250),
	inventory_received_item_cost		varchar(12),
	inventory_on_hand_date			timestamp,
	inventory_on_hand_quantity		varchar(12),
	inventory_on_hand_quantity_unit		varchar(250),
	procedure_code				varchar(705),
	procedure_code_modifier			varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)

);
---------------Shankar code end --------------------------

---------------Fangyu code begin---------------------------
create table ilt (	
	set_id_ilt									integer PRIMARY KEY,
	inventory_lot_number						varchar(250),
	inventory_expiration_date					timestamp,
	inventory_received_date						timestamp,
	inventory_received_quantity 				varchar(12),	
	inventory_received_quantity_unit			varchar(250),
	inventory_received_item_cost				varchar(12),
	inventory_on_hand_date						timestamp,
	inventory_on_hand_quantity 					varchar(12),
	inventory_on_hand_quantity_unit				varchar(250),

	patient_id               					integer,
	foreign key (patient_id) references pid (patient_id)

);
create table in1 (	
	set_id_in1 									integer PRIMARY KEY,
	insurance_plan_id 							varchar(250),
	insurance_company_id						varchar(250),
	insurance_company_name						varchar(250),
	insurance_company_address					varchar(250),
	insurance_co_contact_person 				varchar(250),
	insurance_co_phone_number 					varchar(250),
	group_number 								varchar(12),
	group_name 									varchar(250),
	insured_group_emp_id 						varchar(250),
	insured_group_emp_name 						varchar(250),
	plan_effective_date 						date,
	plan_expiration_date 						date,
	authorization_information 					varchar(239),
	plan_type 									varchar(3),
	name_of_insured 							varchar(250),
	insured_relationship_to_patient 			varchar(250),
	insured_date_of_birth 						timeStamp,
	insured_address 							varchar(250),
	assignment_of_benefits 						integer,
	coordination_of_benefits 					integer,
	coord_of_ben_priority 						integer,
	notice_of_admission_flag 					boolean,
	notice_of_admission_date 					date,
	report_of_eligibility_flag 					boolean,
	report_of_eligibility_date 					integer,
	release_information_code 					varchar(15),
	pre_admit_cert_pac 						varchar(24),
	verification_date_time 						timestamp,
	verification_by 							varchar(250),
	type_of_agreement_code 						integer,
	billing_status 								integer,
	lifetime_reserve_days 						integer,
	delay_before_l_r_day 						integer,
	company_plan_code 							varchar(20),
	policy_number 								varchar(15),
	policy_deductible 							varchar(12),
	policy_limit_amount 						integer,
	policy_limit_days 							integer,
	room_rate_semi_private 						integer,
	room_rate_private 							integer,
	insured_employment_status 					varchar(250),
	insured_administrative_sex 					varchar(1),
	insured_employer_address 					varchar(250),
	verification_status 						integer,
	prior_insurance_plan_id 					integer,
	coverage_type 								varchar(3),
	handicap 									varchar(2),
	insured_id_number 							varchar(250),
	signature_code 								integer,
	signature_code_date	 						date,
	insured_birth_place 						varchar(250),
	vip_indicator 								varchar(2),

	patient_id               					integer,
	foreign key (patient_id) references pid (patient_id)

);

create table in2(	
	insured_employee_id 						varchar(250),
	insured_social_security_number 				varchar(11),
	insured_employer_name_and_id 				varchar(250),
	employer_information_data 					integer,
	mail_claim_party 							integer,
	medicare_health_ins_card_number 			varchar(15),
	medicaid_case_name 							varchar(250),
	medicaid_case_number 						varchar(15),
	military_sponsor_name						varchar(250),
	military_id_number 							varchar(20),
	dependent_of_military_recipient 			varchar(250),
	military_organization						varchar(25),
	military_station							varchar(25),
	military_service 							varchar(14),
	military_rank_grade 						integer,
	military_status 							varchar(3),
	military_retire_date 						date,
	military_non_avail_cert_on_file 			integer,
	baby_coverage								integer,
	combine_baby_bill							integer,
	blood_deductible							varchar(1),
	special_coverage_approval_name				varchar(250),
	special_coverage_approval_title				varchar(30),
	non_covered_insurance_code					varchar(8),
	payor_id 									varchar(250),
	payor_subscriber_id							varchar(250),
	eligibility_source							integer,
	room_coverage_typeamount					varchar(82),
	policy_typeamount 							varchar(56),
	daily_deductible 							varchar(25),
	living_dependency							varchar(2),
	ambulatory_status 							varchar(2),
	citizenship 								varchar(705),
	primary_language 							varchar(705),
	living_arrangement 							varchar(2),
	publicity_code 								varchar(705),
	protection_indicator 						boolean,
	student_indicator 							varchar(2),
	religion 									varchar(705),
	mother_maiden_name 							varchar(250),
	nationality 								varchar(3),
	ethnic_group								varchar(705),
	marital_status 								varchar(705),
	insured_employment_start_date 				date,
	employment_stop_date 						date,
	job_title 	 								varchar(20),
	job_code_class 								varchar(20),
	job_status									varchar(2),
	employer_contact_person_name				varchar(250),
	employer_contact_person_phone_number 		varchar(250),
	employer_contact_reason 					varchar(2),
	insured_contact_person_name					varchar(250),
	insured_contact_person_phone_number 		varchar(250),
	insured_contact_person_reason 				varchar(2),
	relationship_to_the_patient_start_date 		date,
	relationship_to_the_patient_stop_date 		date,
	insurance_co_contact_reason 				varchar(2),
	insurance_co_contact_phone_number 			varchar(250),
	policy_scope 								varchar(2),
	policy_source 								varchar(2),
	patient_member_number 						varchar(250),
	guarantor_relationship_to_insured 			varchar(250),
	insured_phone_number_home					varchar(250),
	insured_employer_phone_number	 			varchar(250),
	military_handicapped_program 				varchar(250),
	suspend_flag								boolean,
	copay_limit_flag							boolean,
	stoploss_limit_flag 						boolean,
	insured_organization_name_and_id 			varchar(250),
	insured_employer_organization_nameand_id    varchar(250),
	race 									 	varchar(705),
	patient_relationship_to_insured 			varchar(705),


	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)

);


create table in3 (	
	set_id_in3									varchar(4) PRIMARY KEY,
	certification_number 						varchar(250), 
	certified_by 							 	varchar(250), 
	certification_required 						varchar(1),
	penalty 									varchar(23), 
	certification_datetime 						timestamp,
	certification_modify_datetime 				timestamp,
	operator 									varchar(250), 
	certification_begin_date 					date,
	certification_end_date 						date,
	days 									    varchar(6),
	non_concur_code_description 				varchar(250), 
	non_concur_effective_datetime 				timestamp,
	physician_reviewer 							varchar(250), 
	certification_contact 						varchar(48), 
	certification_contact_phone_number 			varchar(250), 
	appeal_reason 								varchar(250), 
	certification_agency 						varchar(250), 
	certification_agency_phone_number 			varchar(250), 
	precertification_requirement 				varchar(40), 
	case_manager 								varchar(48), 
	second_opinion_date 						date,
	second_opinion_status 						boolean,
	second_opinion_documentation_received 		boolean,
	second_opinion_physician					varchar(250),

   
	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);
-----------------Fangyu code end----------------------------

---------------  The code below is from Fenhan--------------
---------------  Begin -------------------------------------
create table lnv (
	substance_identifier 							varchar(705),
	substance_status 								varchar(705),
	substance_type 									varchar(705),
	inventory_container_identifier 					varchar(705),
	container_carrier_identifier 					varchar(705),
	position_on_carrier 							varchar(705),
	initial_quantity 								varchar(20),
	current_quantity 								varchar(20),
	available_quantity 								varchar(20),
	consumption_quantity 							varchar(20),
	quantity_units 									varchar(705),
	expiration_date_time 							timestamp,
	first_used_date_time 							timestamp,
	on_board_stability_duration 					varchar(200),
	test_fluid_identifier 							varchar(705),
	manufacturer_lot_number 						varchar(200),
	manufacturer_identifier 						varchar(705),
	supplier_identifier 							varchar(705),
	on_board_stability_time 						varchar(722),
	target_value 									varchar(722),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lpc (
	accession_identifier 							varchar(427),							
	requested_procedure_id 							varchar(22),
	study_instance_uid 								varchar(70),
	scheduled_procedure_step_id 					varchar(22),
	modality 										varchar(16),
	protocol_code 									varchar(250),
	scheduled_station_name 							varchar(22),
	scheduled_procedure_step_location 				varchar(250),
	scheduled_station_ae_title 						varchar(16),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lpr (
	ipr_identifier 									varchar(73),		
	provider_cross_reference_identifier 			varchar(73),
	payer_cross_reference_identifier 				varchar(73),
	ipr_status 										varchar(177),
	ipr_date_time 									timestamp,
	adjudicated_paid_amount 						varchar(254),
	expected_payment_date_time 						timestamp,
	ipr_checksum 									varchar(10),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lsd (	
	reference_interaction_number 					varchar(20),
	interaction_type_identifier 					varchar(705),
	interaction_active_state 						varchar(705),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table ltm (	
	item_identifier 								varchar(250),
	item_description 								varchar(999),
	item_status 									varchar(250),
	item_type 										varchar(250),
	item_category 									varchar(250),
	subject_to_expiration_indicator 				varchar(4),
	manufacturer_identifier 						varchar(250),
	manufacturer_name 								varchar(999),
	manufacturer_catalog_number 					varchar(20),
	manufacturer_labeler_identification_code 		varchar(4),
	patient_chargeable_indicator 					varchar(4),
	transaction_code 								varchar(250),
	transaction_amount_unit 						varchar(12),
	stocked_item_indicator 							varchar(4),
	supply_risk_codes 								varchar(250),
	approving_regulatory_agency 					varchar(250),
	latex_indicator 								varchar(4),
	ruling_act 										varchar(250),
	item_natural_account_code 						varchar(30),
	approved_to_buy_quantity 						integer,
	approved_to_buy_price 							integer,
	taxable_item_indicator 							integer,
	freight_charge_indicator 						integer,
	item_set_indicator 								integer,
	item_set_identifier 							varchar(250),
	track_department_usage_indicator 				integer,
	procedure_code 									varchar(705),
	procedure_code_modifier 						varchar(705),
	special_handling_code 							varchar(705),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table ivc (	
 	provider_invoice_number 						varchar(74),
	payer_invoice_number 							varchar(74),
	contract_agreement_number 						varchar(74), 
	invoice_control									integer,
	invoice_reason 									varchar(4),
	invoice_type 									varchar(2), 									
	invoice_date_time 								timestamp,
	invoice_amount 									varchar(254),
	payment_terms 									varchar(80),
	provider_organization 							varchar(183),
	payer_organization 								varchar(183),
	attention 										varchar(637),
	last_invoice_indicator 							integer,
	invoice_booking_period 							timestamp,
	origin 											varchar(250),
	invoice_fixed_amount 							varchar(254),
	special_costs 									varchar(254),
	amount_for_doctors_treatment 					varchar(254),
	responsible_physician 							varchar(250),
	cost_center 									varchar(250),
	invoice_prepaid_amount 							varchar(254),
	total_invoice_amount_without_prepaid_amount 	varchar(254),
	total_amount_of_vat 							varchar(254),
	vat_rates_applied 								varchar(1024),
	benefit_group 									varchar(4),
	provider_tax_id 								varchar(20),
	payer_tax_id 									varchar(20),
	provider_tax_status 							varchar(4),
	payer_tax_status 								varchar(4),
	sales_tax_id 									varchar(20),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table ivt (	
	set_id_ivt 										integer primary key,
	inventory_location_identifier 					varchar(250),
	inventory_location_name  						varchar(250),						
	source_location_identifier 	 					varchar(250),				
	source_location_name 							varchar(250),
	item_status 									varchar(250),
	bin_location_identifier 	 					varchar(250),
	order_packaging 								varchar(250),
	issue_packaging 								varchar(250),
	default_inventory_asset_account 				varchar(16),
	patient_chargeable_indicator 					varchar(4),
	transaction_code 								varchar(250),
	transaction_amount_unit 						varchar(12),
	item_importance_code 							varchar(250),
	stocked_item_indicator 							varchar(4),
	consignment_item_indicator 						varchar(4),
	reusable_item_indicator 						varchar(4),
	reusable_cost 									varchar(12),
	substitute_item_identifier 						varchar(250),
	latex_free_substitute_item_identifier   		varchar(250),
	recommended_reorder_theory 						varchar(250),
	recommended_safety_stock_days 					integer,
	recommended_maximum_days_inventory 				integer,
	recommended_order_point 						integer,
	recommended_order_amount 						integer,
	operating_room_par_level_indicator 				varchar(4),


	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lan (	
	set_id_lan 										varchar(60) primary key,
	language_code 									varchar(250),
	language_ability_code 							varchar(250),
	language_proficiency_code 						varchar(250),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lcc (	
	primary_key_value_lcc 							varchar(200) primary key,
	location_department 							varchar(250),
	accommodation_type 								varchar(250),
	charge_code 									varchar(250),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lch (	
	primary_key_value_lch 							varchar(200) primary key,
	segment_action_code 							integer,
	segment_unique_key 								varchar(80),
	location_characteristic_id 						varchar(250),
	location_characteristic_value_lch 				varchar(250),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table ldp (	
	primary_key_value_ldp 							varchar(200) primary key,
	location_department 							varchar(250),
	location_service 								varchar(3),
	specialty_type 									varchar(250),
	valid_patient_classes 							varchar(1),
	active_inactive_flag 							integer,
	activation_date_ldp 							timestamp,
	inactivation_date_ldp 							timestamp,
	inactivated_reason 								varchar(80),
	visiting_hours 									varchar(80),
	contact_phone 									varchar(250),
	location_cost_center 							varchar(250),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table loc (	
	primary_key_value_loc 							varchar(200) primary key,
	location_description 							varchar(48),
	location_type_loc 								varchar(2),
	organization_name_loc 							varchar(250),
	location_address 								varchar(250),
	location_phone 									varchar(250),
	license_number 									varchar(250),
	location_equipment 								varchar(3),
	location_service_code 							integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table lrl (	
	primary_key_value_lrl 							varchar(200) primary key,
	segment_action_code 							integer,
	segment_unique_key 								varchar(80),
	location_relationship_id 						varchar(250),
	organizational_location_relationship_value 		varchar(250),
	patient_location_relationship_value 			varchar(80),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table mfa (	
	record_level_event_code 						integer,
	mfn_control_id 									varchar(20),
	event_completion_date_time 						timestamp,
	mfn_record_level_error_return 					varchar(250),
	primary_key_value_mfa 							varchar(250),
	primary_key_value_type_mfa 						integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table mfe (	
	record_level_event_code 						integer,				
	mfn_control_id 									varchar(20),
	effective_date_time 							timestamp,
	primary_key_value_mfe 							varchar(200),
	primary_key_value_type 							integer,
	entered_date_time 								timestamp,
	entered_by 										varchar(3220),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table mfi (	
	master_file_identifier 							varchar(250),
	master_file_application_identifier 				varchar(180),
	file_level_event_code 							integer,
	entered_date_time 								timestamp,
	effective_date_time 							timestamp,
	response_level_code 							integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table mrg (	
	prior_patient_identifier_list 					varchar(250),
	prior_alternate_patient_id 						varchar(250),
	prior_patient_account_number 					varchar(250),
	prior_patient_id 								varchar(250),
	prior_visit_number 								varchar(250),
	prior_alternate_visit_id 						varchar(250),
	prior_patient_name 							 	varchar(250),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table msa (	
	acknowledgment_code 							integer,
	message_control_id 								varchar(199),
	text_message 									integer,
	expected_sequence_number 						varchar(15),
	delayed_acknowledgment_type 					varchar(200),
	error_condition 								varchar(200),
	message_waiting_number 							integer,
	message_waiting_priority 						integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table msh (	
	field_separator 								varchar(1),
	encoding_characters 							varchar(4), 
	sending_application 							varchar(277),
	sending_facility 								varchar(277),
	receiving_application 							varchar(277),
	receiving_facility 								varchar(277),
	date_time_of_message 							timestamp,
	security 										varchar(40),
	message_type 									varchar(15),
	message_control_id 								varchar(199),
	processing_id 									varchar(3),
	version_id 										varchar(60),
	sequence_number 								varchar(15),
	continuation_pointer 							varchar(180),
	accept_acknowledgment_type 						integer,
	application_acknowledgment_type 				integer,
	country_code 									integer,
	character_set 									varchar(16),
	principal_language_of_message 					varchar(250),
	alternate_character_set_handling_scheme 		varchar(20),
	message_profile_identifier 						varchar(427),
	sending_responsible_organization 				varchar(567),
	receiving_responsible_organization 				varchar(567),
	sending_network_address 						varchar(227),
	receiving_network_address 						varchar(227),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table nck (	
	system_date_time 								timestamp,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table nds (	
	notification_reference_number 					integer,
	notification_date_time 							timestamp,
	notification_alert_severity 					varchar(705),
	notification_code 								varchar(705),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table nk1 (	
	set_id_nk1 										integer primary key,
	name 											varchar(250),
	relationship 									varchar(705),
	address 										varchar(250),
	phone_number 									varchar(250),
	business_phone_number 							varchar(250),
	contact_role 									varchar(705),
	start_date 										timestamp,
	end_date 										timestamp,
	next_of_kin_associated_parties_job_title 		varchar(80),
	next_of_kin_associated_parties_job_code_class 	varchar(20),
	next_of_kin_associated_parties_employee_number 	varchar(250),
	organization_name_nk1 							varchar(250),
	marital_status 									varchar(705),
	administrative_sex 								integer,
	date_time_of_birth 								timestamp,
	living_dependency 								varchar(2),
	ambulatory_status 								varchar(2),
	citizenship 									varchar(705),
	primary_language 								varchar(705),
	living_arrangement 								integer,
	publicity_code 									varchar(705),
	protection_indicator 							integer,
	student_indicator 								integer,
	religion 										varchar(705),
	mother_maiden_name 								varchar(250),
	nationality 									varchar(200),
	ethnic_group 									varchar(705),
	contact_reason 									varchar(705),
	contact_person_name 							varchar(250),
	contact_person_telephone_number 				varchar(250),
	contact_person_address 							varchar(250),
	next_of_kin_associated_party_identifiers 		varchar(250),
	job_status 										integer,
	race 											varchar(705),
	handicap 										integer,
	contact_person_social_security_number 			varchar(16),
	next_of_kin_birth_place 						varchar(250),
	vip_indicator 									integer,
 			
	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table npu (	
	bed_location 									varchar(80),
	bed_status 									  	integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table nsc (	
	application_change_type 						integer,
	current_cpu 									varchar(30),
	current_fileserver 								varchar(30),
	current_application 							varchar(30),
	current_facility 								varchar(30),
	new_cpu 										varchar(30),
	new_fileserver 									varchar(30),
	new_application 								varchar(30),
	new_facility 									varchar(30),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table nst (	
	statistics_available							integer,
	source_identifier 								varchar(30),
	source_type 									integer,
	statistics_start 								timestamp,
	statistics_end 									timestamp,
	receive_character_count 						integer,
	send_character_count 							integer,
	messages_received 								integer,
	messages_sent 									integer,
	checksum_errors_received 						integer,
	length_errors_received 							integer,
	other_errors_received 							integer,
	connect_timeouts 								integer,
	receive_timeouts 								integer,
	application_control_level_errors 				integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table nte (	
	set_id_nte 										integer primary key,
	source_of_comment 								integer, 								
	comment 										long varchar(65536),
	comment_type 									varchar(250),
	entered_by 										varchar(3220),
	entered_date_time 								timestamp,
	effective_start_date 							timestamp,
	expiration_date 								timestamp,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table obr (	
	set_id_obr 										integer primary key,
	placer_order_number 							varchar(427),
	filler_order_number 							varchar(427),
	universal_service_identifier 					varchar(705),
	priority 										integer,
	requested_date_time 							timestamp,
	observation_date_time 							timestamp,
	observation_end_date_time 						timestamp,
	collection_volume 								varchar(722),
	collector_identifier 							varchar(3220),
	specimen_action_code 							integer,
	danger_code 									varchar(705),
	relevant_clinical_information 					varchar(300),
	specimen_received_date_time 					timestamp,
	specimen_source 								varchar(200),
	ordering_provider 								varchar(3220),
 	order_callback_phone_number 					varchar(2734),
	placer_field1 									varchar(200),
	placer_field2 									varchar(200),
	filler_field_1 									varchar(200),
	filler_field_2 									varchar(200),
	results_rpt_status_chng_date_time 				timestamp,
	charge_to_practice 								varchar(504), 							
	diagnostic_serv_sect_id 						integer,
	result_status 									integer,
	parent_result 									varchar(977),
	quantity_timing 								varchar(20),
	result_copies_to 								varchar(3220),
	parent 											varchar(855),
	transportation_mode 							varchar(20),
	reason_for_study 								varchar(705),
	principal_result_interpreter 					varchar(50),
	assistant_result_interpreter 					varchar(50),
	technician 										varchar(50),
	transcriptionist 								varchar(50),
	scheduled_date_time 							timestamp,
	number_of_sample_containers 					varchar(16),
	transport_logistics_of_collected_sample 		varchar(705),
	collector_comment 								varchar(705),
	transport_arrangement_responsibility 			varchar(705),
	transport_arranged 								varchar(30),
	escort_required 								integer,
	planned_patient_transport_comment 				varchar(705),
	procedure_code 									varchar(705),
	procedure_code_modifier 						varchar(705),
	placer_supplemental_service_information 		varchar(705),
	filler_supplemental_service_information 		varchar(705),
	medically_necessary_duplicate_procedure_reason 	varchar(705),
	result_handling 								integer,
	parent_universal_service_identifier 			varchar(705),
 					
	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table obx (	
	set_id_obx 										integer primary key,
	value_type 										integer,
	observation_identifier 							varchar(705),
	observation_sub_id 								varchar(20),
	observation_value 								varchar(581),
	units 											varchar(705),
	references_range 								varchar(60),
	abnormal_flags 									integer,
	probability 									integer,
	nature_of_abnormal_test 						integer,
	observation_result_status 						integer,
	effective_date_of_reference_range 				timestamp,
	user_defined_access_checks 						varchar(20),
	date_time_of_the_observation 					timestamp,
	producer_id 									varchar(705),
	responsible_observer 							varchar(3220),
	observation_method 								varchar(705),
	equipment_instance_identifier 					varchar(415),
	date_time_of_the_analysis 						timestamp,
	observation_site 								varchar(705),
	observation_instance_identifier 				varchar(427),
	mood_code 										varchar(705),
	performing_organization_name 					varchar(570),
	performing_organization_address 				varchar(2915),
	performing_organization_medical_director 		varchar(3220),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table ods (	
	type 											integer,
	service_period 									varchar(250),
	diet_supplement_or_preference_code 				varchar(250),
	text_instruction 								varchar(80),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table odt (	
	tray_type 										varchar(250),
	service_period 									varchar(250),
	text_instruction 								varchar(80),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table om1 (	
	sequence_number_test_observation_master_file	 integer,
	producer_service_test_observation_id			 varchar(250), 			
	permitted_data_types 						     integer,
	specimen_required 								 integer,
	producer_id 								     varchar(250),
	observation_description 						 varchar(200),
	other_service_test_observation_ids_for_the_observation 		varchar(250),
	other_names 									 varchar(200),
	preferred_report_name_for_the_observation 		 varchar(30),
	preferred_short_name_or_mnemonic_for_observation varchar(8),
	preferred_long_name_for_the_observation 		 varchar(200),
	orderability 									 integer,
	identity_of_instrument_used_to_perform_this_study varchar(250),
	coded_representation_of_method 					 varchar(250),
	portable_device_indicator 						 integer,
	observation_producing_department_section 		 varchar(250),
	telephone_number_of_section 					varchar(250),
	nature_of_service_test_observation 				 integer,	
	report_subheader 								varchar(250),
	report_display_order 							varchar(20),
	date_time_stamp_for_any_change_in_definition_for_the_observation  timestamp,
	effective_date_time_of_change   				timestamp,
	typical_turn_around_time 						integer,
	processing_time 								 integer,
	processing_priority								varchar(40),
	reporting_priority 								varchar(5),
	outside_site_where_observation_may_be_performed varchar(250),	
	address_of_outside_site 						varchar(250),
	phone_number_of_outside_site 					varchar(250),
	confidentiality_code 							varchar(250),
	observations_required_to_interpret_the_observation	varchar(250),
	interpretation_of_observations 					long varchar(65536),
	contraindications_to_observations 				varchar(250),
	reflex_tests_observations 						varchar(250),
	rules_that_trigger_reflex_testing 				varchar(80),
	fixed_canned_message 							varchar(250),
	patient_preparation 							varchar(200),
	procedure_medication 							varchar(250),
	factors_that_may_affect_the_observation 		varchar(200),
	service_test_observation_performance_schedule 	varchar(60),
	description_of_test_methods 					long varchar(65536),
	kind_of_quantity_observed 						varchar(250),
	point_versus_interval 							varchar(250),
	challenge_information 							varchar(200),
	relationship_modifier 							varchar(200),
	target_anatomic_site_of_test 					varchar(250),
	modality_of_imaging_measurement 				varchar(250),
 					

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table om2 (	
	sequence_number_test_observation_master_file 	integer,
	units_of_measure 								varchar(250),
	range_of_decimal_precision 						varchar(10),
	corresponding_si_units_of_measure 				varchar(250),
	si_conversion_factor 							varchar(60),
	reference_normal_range_for_ordinal_and_continuous_observations 	varchar(250), 	
	critical_range_for_ordinal_and_continuous_observations 				varchar(205),
	absolute_range_for_ordinal_and_continuous_observations 				varchar(250),
	delta_check_criteria 							varchar(250),
	minimum_meaningful_increments 					varchar(20),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table om3 (	
	sequence_number_test_observation_master_file 	integer,
	preferred_coding_system 						varchar(250),
	valid_coded_answers 							varchar(250),
	normal_text_codes_for_categorical_observations 	varchar(250),
	abnormal_text_codes_for_categorical_observations varchar(250),
	critical_text_codes_for_categorical_observations varchar(250),
	value_type 										integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table om4 (	
	sequence_number_test_observation_master_file 	integer,
	derived_specimen 								integer,
	container_description 							varchar(60),
	container_volume 								varchar(20),
	container_units 								varchar(250),
	specimen 										varchar(250),
	additive 										varchar(705),
	preparation 									varchar(10240),
	special_handling_requirements 					varchar(10240),
	normal_collection_volume 						varchar(20),
	minimum_collection_volume 						varchar(20),
	specimen_requirements 							varchar(10240),
	specimen_priorities 							integer,
	specimen_retention_time 						integer,

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table om5 (	
	sequence_number_test_observation_master_file 	integer,
	test_observations_included_within_an_ordered_test_battery varchar(250),
	observation_id_suffixes 						varchar(250),

	patient_id               						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table om6 (	
	sequence_number_test_observation_master_file 	integer,
	derivation_rule 								varchar(10240),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table om7 (	
	sequence_number_test_observation_master_file 	integer,
	universal_service_identifier 					varchar(705),
	category_identifier 							varchar(250),
	category_description 							varchar(200),
	category_synonym 								varchar(200),
	effective_test_service_start_date_time 			timestamp,
	effective_test_service_end_date_time 			timestamp,
	test_service_default_duration_quantity 			integer,
	test_service_default_duration_units 			varchar(250),
	test_service_default_frequency 					varchar(60),
	consent_indicator 								integer,
	consent_identifier 								varchar(250),
	consent_effective_start_date_time 				timestamp,
	consent_effective_end_date_time 				timestamp,
	consent_interval_quantity 						integer,
	consent_interval_units 							varchar(250),
	consent_waiting_period_quantity 				integer,
	consent_waiting_period_units 					varchar(250),
	effective_date_time_of_change 					timestamp,
	entered_by 										varchar(3220),
	orderable_at_location 							varchar(200),
	formulary_status 								integer,
	special_order_indicator 						integer,
	primary_key_value_cdm 							varchar(250),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table orc (	
	order_control 									integer,
	placer_order_number 							varchar(427),
	filler_order_number 							varchar(427),
	placer_group_number 							varchar(22),
	order_status 									integer,
	response_flag 									integer,
	quantity_timing 								varchar(1000),
	parent 											varchar(200),
	date_time_of_transaction 						timestamp,
	entered_by 										varchar(3220),
	verified_by 									varchar(250),
	ordering_provider 								varchar(3220),
	enterer_location 								varchar(80),
	call_back_phone_number 							varchar(250),
	order_effective_date_time 						timestamp,
	order_control_code_reason 						varchar(250),
	entering_organization 							varchar(250),
	entering_device 								varchar(250),
	action_by 										varchar(250),
	advanced_beneficiary_notice_code 				varchar(250),
	ordering_facility_name 							varchar(250),
	ordering_facility_address 						varchar(250),
	ordering_facility_phone_number 					varchar(250),
	ordering_provider_address 						varchar(250),
	order_status_modifier 							varchar(250),
	advanced_beneficiary_notice_override_reason 	varchar(60),
	filler_expected_availability_date_time 			timestamp,
	confidentiality_code 							varchar(250),
	order_type 										varchar(250),
	enterer_authorization_mode 						varchar(250),
	parent_universal_service_identifier 			varchar(250),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table org (	
	set_id_org 										varchar(60) primary key,
	organization_unit_code 							varchar(250),
	organization_unit_type_code 					varchar(250),
	primary_org_unit_indicator 						integer,
	practitioner_org_unit_identifier 				varchar(60),
	health_care_provider_type_code 					varchar(250),
	health_care_provider_classification_code 		varchar(250),
	health_care_provider_area_of_specialization_code varchar(250),
	effective_date_range 							varchar(52),
	employment_status_code 							varchar(250),
	board_approval_indicator 						integer,
	primary_care_physician_indicator 				integer,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table ovr (	
	business_rule_override_type 					varchar(705),
	business_rule_override_code 					varchar(705),
	override_comments 								varchar(200),
	override_entered_by 							varchar(250),
	override_authorized_by 							varchar(250),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pce (	
	set_id_pce 										integer,
	cost_center_account_number 						varchar(30),
	transaction_code 								varchar(250),
	transaction_amount_unit 						varchar(12),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pcr (	
	implicated_product 								varchar(705),
	generic_product 								integer,
	product_class 									varchar(705),
	total_duration_of_therapy 						varchar(500),
	product_manufacture_date 						timestamp,
	product_expiration_date 						timestamp,
	product_implantation_date 						timestamp,
	product_explantation_date 						timestamp,
	single_use_device 								varchar(8),
	indication_for_product_use 						varchar(705),
	product_problem 								varchar(8),
	product_serial_lot_number 						varchar(199),
	product_available_for_inspection 				integer,
	product_evaluation_performed 					varchar(705),
	product_evaluation_status 						varchar(705),
	product_evaluation_results 						varchar(705),
	evaluated_product_source 						timestamp,
	date_product_returned_to_manufacturer 			integer,
	device_operator_qualifications 					integer,
	relatedness_assessment 							integer,
	action_taken_in_response_to_the_event 			integer,
	event_causality_observations 					integer,
	indirect_exposure_mechanism 					integer,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pd1 (	
	living_dependency								varchar(2),
	living_arrangement								varchar(2),
	patient_primary_facility						varchar(250),
	patient_primary_care_provider_name_id_no	 	varchar(250),
	student_indicator 								varchar(250),
	handicap 										varchar(2),
	living_will_code 								varchar(2),
	organ_donor_code 								varchar(2),
	separate_bill 									integer,
	duplicate_patient 								varchar(250),
	publicity_code 									varchar(705),
	protection_indicator 							integer,
	protection_indicator_effective_date 			timestamp,
	place_of_worship 								varchar(250),
	advance_directive_code 							varchar(705),
	immunization_registry_status 					integer,
	immunization_registry_status_effective_date 	timestamp,
	publicity_code_effective_date 					timestamp,
	military_branch 								varchar(5),
	military_rank_grade 							varchar(2),
	military_status 								varchar(3),
	advance_directive_last_verified_date 			timestamp,


	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pda (	
	death_cause_code 								varchar(705),
	death_location 									varchar(80),
	death_certified_indicator 						integer,
	death_certificate_signed_date_time 				timestamp,
	death_certified_by 								varchar(250),
	autopsy_indicator 								integer,
	autopsy_start_and_end_date_time 				integer,
	autopsy_performed_by 							varchar(250),
	coroner_indicator 								integer,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pdc (	
	manufacturer_distributor 						varchar(570),
	country 										varchar(705),
	brand_name 										varchar(60),
	device_family_name 								varchar(60),
	generic_name 									varchar(705),
	model_identifier 								varchar(60),
	catalogue_identifier 							varchar(60),
	other_identifier 								varchar(60),
	product_code 									varchar(705),
	marketing_basis 								integer,
	marketing_approval_id 							varchar(60),
	labeled_shelf_life 								varchar(722),
	expected_shelf_life 							varchar(722),
	date_first_marketed 							timestamp,
	date_last_marketed 								timestamp,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table peo (	
	event_identifiers_used 							varchar(705),
	event_symptom_diagnosis_code 					varchar(705),
	event_onset_date_time 							timestamp,
	event_exacerbation_date_time 					timestamp,
	event_improved_date_time 						timestamp,
	event_ended_data_time 							timestamp,
	event_location_occurred_address 				varchar(2915),
	event_qualification 							integer,
	event_serious 									integer,
	event_expected 									integer,
	event_outcome 									integer,
	patient_outcome 								integer,
	event_description_from_others 					varchar(600),
	event_description_from_original_reporter 		varchar(600),
	event_description_from_patient 					varchar(600),
	event_description_from_practitioner 			varchar(600),
	event_description_from_autopsy 					varchar(600),
	cause_of_death 									varchar(705),
	primary_observer_name							varchar(1317),
	primary_observer_address 	 	 				varchar(2915),
	primary_observer_telephone 						varchar(2743),
	primary_observers_qualification 				integer,
	confirmation_provided_by						integer,
	primary_observer_aware_date_time 				timestamp,
	primary_observer_identity_may_be_divulged 		integer,


	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table pes (	
	sender_organization_name						varchar(567),
	sender_individual_name 							varchar(3220),
	sender_address 									varchar(2915),
	sender_telephone 								varchar(2743),
	sender_event_identifier 						varchar(427),
	sender_sequence_number 							varchar(16),
	sender_event_description 						varchar(600),
	sender_comment 									varchar(600),
	sender_aware_date_time 							timestamp,
	event_report_date 								timestamp,
	event_report_timing_type 						integer,
	event_report_source 							integer,
	event_reported_to 								integer,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pkg (	
	set_id_pkg 										varchar(2) primary key, 										
	packaging_units 								varchar(250),
	default_order_unit_of_measure_indicator 		varchar(1),
	package_quantity 								varchar(12),
	price 											varchar(12),
	future_item_price 								varchar(12),
	future_item_price_effective_date 				timestamp,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pmt (	
	payment_remittance_advice_number 				varchar(73),
	payment_remittance_effective_date_time 			timestamp,
	payment_remittance_expiration_date_time 		timestamp,
	payment_method 									varchar(177),
	payment_remittance_date_time 					timestamp,
	payment_remittance_amount 						varchar(256),
	check_number 									varchar(15),
	payee_bank_identification 						varchar(6),
	payee_transit_number 							varchar(4),
	payee_bank_account_id 							varchar(20),
	payment_organization 							varchar(183),
	esr_code_line 									varchar(100),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pr1 (	
	set_id_pr1 										varchar(4),
	procedure_coding_method 						varchar(4),
	procedure_code 									varchar(705),
	procedure_description 							varchar(705),
	procedure_date_time 							timestamp,
	procedure_functional_type 						varchar(2),
	procedure_minutes 								integer,
	anesthesiologist 								varchar(8),
	anesthesia_code 								varchar(2),
	anesthesia_minutes 								integer,
	surgeon 										varchar(500),--no record in the Excel table,
	procedure_practitioner 							varchar(500),--no record in the Excel table,
	consent_code 									varchar(250),
	procedure_priority 								integer,
	associated_diagnosis_code 						varchar(250),
	procedure_code_modifier 						varchar(705),
	procedure_drg_type 								varchar(20),
	tissue_type_code 								varchar(250),
	procedure_identifier 							varchar(427),
	procedure_action_code 							integer,
	drg_procedure_determination_status 				varchar(20),
	drg_procedure_relevance 						varchar(20),


	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table pra (	
	primary_key_value_pra 							varchar(250),
	practitioner_group 								varchar(250),
	practitioner_category 							varchar(3),
	provider_billing 								integer,
	specialty 										varchar(112),
	practitioner_id_numbers 						varchar(20),
	privileges 										varchar(770),
	date_entered_practice 							timestamp,
	institution 									varchar(250),
	date_left_practice 								timestamp,
	government_reimbursement_billing_eligibility 	varchar(250),
	set_id_pra 										varchar(60),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table prb (
	action_code 									integer,
	action_date_time 								timestamp,
	problem_id 										varchar(705),
	problem_instance_id 							varchar(60),
	episode_of_care_id 								varchar(60),
	problem_list_priority 							varchar(60),
	problem_established_date_time 					timestamp,
	anticipated_problem_resolution_date_time 		timestamp,
	actual_problem_resolution_date_time 			timestamp,
	problem_classification 							varchar(705),
	problem_management_discipline 					varchar(705),
	problem_persistence 							varchar(705),
	problem_confirmation_status 					varchar(705),
	problem_life_cycle_status 						varchar(705),
	problem_life_cycle_status_date_time 			timestamp,
	problem_date_of_onset 							timestamp,
	problem_onset_text 								varchar(80),
	problem_ranking 								varchar(705),
	certainty_of_problem 							varchar(705),
	probability_of_problem_oneOrzero 				integer,
	individual_awareness_of_problem 				varchar(705),
	problem_prognosis 								varchar(705),
	individual_awareness_of_prognosis 				varchar(705),
	family_significant_other_awareness_of_problem_prognosis 	varchar(200),
	security_sensitivity 							varchar(705),
	problem_severity 								varchar(705),
	problem_perspective 							varchar(705),
	mood_code 										varchar(60),


	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table prc (
	primary_key_value_prc 							varchar(250),
	facility_id_prc 								varchar(250),
	department 										varchar(250),
	valid_patient_classes 							integer,
	price 											varchar(12),	
	formula 										varchar(200),
	minimum_quantity 								integer,
	maximum_quantity 								integer,
	minimum_price 									varchar(12),--FloatReal	Number	Float	Numeric or currency data type
	maximum_price 									varchar(12),
	effective_start_date 							timestamp,
	effective_end_date 								timestamp,
	price_override_flag 							boolean,
	billing_category 								varchar(250),
	chargeable_flag 								integer,
	active_inactive_flag 							boolean,
	cost 											varchar(12),--FloatReal	Number	Float	Numeric or currency data type
	charge_on_indicator 							boolean,

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);


create table prd (
	provider_role 									varchar(705),
	provider_name 									varchar(250),
	provider_address 								varchar(250),
	provider_location 								varchar(60),
	provider_communication_information 				varchar(250),
	preferred_method_of_contact 					varchar(705),
	provider_identifiers 							varchar(100),
	effective_start_date_of_provider_role 			timestamp,
	effective_end_date_of_provider_role 			timestamp,
	provider_organization_name_and_identifier 		varchar(250),
	provider_organization_address 					varchar(60),
	provider_organization_location_information		varchar(60),
	provider_organization_communication_information varchar(250),
	provider_organization_method_of_contact 		varchar(705),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table psh (
	report_type 									varchar(60),
	report_form_identifier 							varchar(60),
	report_date 									timestamp,
	report_interval_start_date 						timestamp,
	report_interval_end_date 						timestamp,
	quantity_manufactured 							varchar(722),
	quantity_distributed 							varchar(722),
	quantity_distributed_method 					integer,
	quantity_distributed_comment 					varchar(600),
	quantity_in_use 								varchar(722),
	quantity_in_use_method 							integer,
	quantity_in_use_comment 						varchar(600),
	number_of_product_experience_reports_filed_by_facility 	varchar(16),
	number_of_product_experience_reports_filed_by_distributor	varchar(16),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);	

create table psl (
	provider_product_service_line_item_number 		varchar(73),
	payer_product_service_line_item_number 			varchar(73),
	product_service_line_item_sequence_number 		integer,
	provider_tracking_id 							varchar(20),
	payer_tracking_id 								varchar(20),
	product_service_line_item_status 				varchar(2),
	product_service_code 							varchar(177),
	product_service_code_modifier 					varchar(177),
	product_service_code_description 				varchar(80),
	product_service_effective_date 					timestamp,
	product_service_expiration_date 				timestamp,
	product_service_quantity 						varchar(222),
	product_service_unit_cost 						varchar(254),
	number_of_items_per_unit 						integer,
	product_service_gross_amount 					varchar(254),
	product_service_billed_amount 					varchar(254),
	product_service_clarification_code_type 		varchar(10),
	product_service_clarification_code_value 		varchar(40),
	health_document_reference_identifier 			varchar(73),
	processing_consideration_code 					varchar(10),
	restricted_disclosure_indicator					integer,
	related_product_service_code_indicator 			varchar(177),
	product_service_amount_for_physician 			varchar(254),
	product_service_cost_factor 					integer,
	cost_center 									varchar(250),
	billing_period 									varchar(49),
	days_without_billing 							integer,
	session_no 										integer,
	executing_physician_id 							varchar(20),
	responsible_physician_id 						varchar(20),
	role_executing_physician 						varchar(10),
	medical_role_executing_physician 				varchar(10),
	side_of_body 									varchar(3),
	number_of_tp_pp 								integer,
	tp_value_pp										varchar(6),
	internal_scaling_factor_pp 						integer,
	external_scaling_factor_pp 						integer,
	amount_pp 										varchar(7),								
	number_of_tp_technical_part 					integer,
	tp_value_technical_part 						varchar(6),
	internal_scaling_factor_technicalpart 			integer,
	external_scaling_factor_technicalpart			integer,
	amount_technical_part 							varchar(7),
	total_amount_professional_part_technical_part 	varchar(8),
	vat_rate 										integer,									
	main_service 									varchar(20),
	validation 										integer,
	comment 										varchar(255),

	patient_id                						integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pss (
	provider_product_service_section_number 		varchar(73),
	payer_product_service_section_number 			varchar(73),
	product_service_section_sequence_number 		varchar(4),
	billed_amount 									varchar(254),
	section_description_or_heading 					varchar(254),

	patient_id                	integer,
	foreign key (patient_id) references pid (patient_id)
);


create table pth (
	action_code 				integer,
	pathway_id 					varchar(705),
	pathway_instance_id 		varchar(60),
	pathway_established_date_time 	timestamp,
	pathway_life_cycle_status 	varchar(705),
	change_pathway_life_cycle_status_date_time	timestamp,
	mood_code 					varchar(60),

	patient_id                	integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pv1 (
	set_id_pv1					varchar(4) primary key,
	patient_class 				integer,
	assigned_patient_location 	varchar(80),
	admission_type 				integer,
	preadmit_number 			varchar(250),
	prior_patient_location 		varchar(80),
	attending_doctor 			varchar(250),
	referring_doctor 			varchar(250),
	consulting_doctor 			varchar(250),
	hospital_service 			varchar(3),
	temporary_location 			varchar(80),
	preadmit_test_indicator 	varchar(2),
	re_admission_indicator 		varchar(2),
	admit_source 				varchar(6),
	ambulatory_status 			varchar(6),
	vip_indicator 				varchar(2),
	admitting_doctor 			varchar(250),
	patient_type 				varchar(2),
	visit_number 				varchar(250),
	financial_class 			varchar(50),
	charge_price_indicator 		varchar(2),
	courtesy_code 				varchar(2),
	credit_rating 				varchar(2),
	contract_code 				varchar(2),
	contract_effective_date 	timestamp,
	contract_amount 			integer,
	contract_period 			integer,
	interest_code 				varchar(2),
	transfer_to_bad_debt_code 	varchar(2),
	transfer_to_bad_debt_date 	timestamp,
	bad_debt_agency_code 		varchar(10),
	bad_debt_transfer_amount	varchar(12),
	bad_debt_recovery_amount 	varchar(12),
	delete_account_indicator 	integer,
	delete_account_date 		timestamp,
	discharge_disposition 		varchar(3),
	discharged_to_location 		varchar(47),
	diet_type 					varchar(705),
	servicing_facility 			varchar(2),
	bed_status 					integer,
	account_status 				integer,
	pending_location 			varchar(80),
	prior_temporary_location 	varchar(80),
	admit_date_time 			timestamp,
	discharge_date_time 		timestamp,
	current_patient_balance 	varchar(12),
	total_charges 				varchar(12),
	total_adjustments 			varchar(12),
	total_payments 				varchar(12),
	alternate_visit_id			varchar(250),
	visit_indicator 			boolean,
	other_healthcare_provider 	varchar(255),

	patient_id              	integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pv2 (
	prior_pending_location 			varchar(80),		
	accommodation_code 				varchar(705),
	admit_reason 					varchar(705),
	transfer_reason 				varchar(705),	
	patient_valuables 				varchar(25),
	patient_valuables_location 		varchar(25),
	visit_user_code 				varchar(2),
	expected_admit_date_time 		timestamp,
	expected_discharge_date_time 	timestamp,
	estimated_length_of_inpatient_stay 	integer,
	actual_length_of_inpatient_stay 	integer,	
	visit_description 				varchar(50),
	referral_source_code 			varchar(250),
	previous_service_date 			timestamp,
	employment_illness_related_indicator 	integer,
	purge_status_code 				integer,
	purge_status_date 				timestamp,
	special_program_code 			integer,
	retention_indicator 			boolean,
	expected_number_of_insurance_plans 	integer,
	visit_publicity_code 			integer,
	visit_protection_indicator 		integer,
	clinic_organization_name 		varchar(250),
	patient_status_code 			integer,
	visit_priority_code 			integer,
	previous_treatment_date 		timestamp,
	expected_discharge_disposition 	integer,
	signature_on_file_date 			timestamp,
	first_similar_illness_date 		timestamp,
	patient_charge_adjustment_code 	varchar(205),
	recurring_service_code 			integer,
	billing_media_code 				integer, 	
	expected_surgery_date_and_time 	timestamp,
	military_partnership_code 		integer,
	military_non_availability_code 	integer,
	newborn_baby_indicator 			integer,
	baby_detained_indicator 		integer,
	mode_of_arrival_code 			varchar(705),
	recreational_drug_use_code 		varchar(705),
	admission_level_of_care_code 	varchar(705),
	precaution_code 				varchar(705),
	patient_condition_code 			varchar(705),
	living_will_code 				integer,
	organ_donor_code 				integer,
	advance_directive_code 			varchar(705),
	patient_status_effective_date 	timestamp,
	expected_loa_return_date_time 	timestamp,
	expected_pre_admission_testing_date_time 	timestamp,
	notify_clergy_code 				integer,
	advance_directive_last_verified_date 	timestamp,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table pye (
	set_id_pye 						integer primary key,
	payee_type 						varchar(6),
	payee_relationship_to_invoice 	varchar(2),
	payee_identification_list 		varchar(183),
	payee_person_name 				varchar(466),
	payee_address 					varchar(235),
	payment_method 					varchar(80),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table qak (
	query_tag 						varchar(32),
	query_response_status 			integer,
	message_query_name 				varchar(250),
	hit_count_total 				integer,
	this_payload 					varchar(250),
	hits_remaining 					varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table qid (
	query_tag 						varchar(32),
	message_query_name 				varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);


create table qpd (
	message_query_name 				varchar(250),
	query_tag 						varchar(32),
	user_parameters 				varchar(256),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table qrd (
	query_date_time 				timestamp,
	query_format_code 				integer,
	query_priority 					integer,
	query_id 						varchar(10),
	deferred_response_type 			integer,
	deferred_response_date_time 	timestamp,
	quantity_limited_request 		varchar(10),
	who_subject_filter 				varchar(250),
	what_subject_filter 			varchar(250),	
	what_department_data_code 		varchar(250),
	what_data_code_value_qual 		varchar(20),
	query_results_level 			integer,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table qrf (
	where_subject_filter 			varchar(20),
	when_data_start_date_time 		timestamp,
	when_data_end_date_time 		timestamp,
	what_user_qualifier 			varchar(60),
	other_qry_subject_filter 		varchar(60),
	which_date_time_qualifier 		varchar(12),
	which_date_time_status_qualifier	varchar(12),
	date_time_selection_qualifier 	varchar(12),
	when_quantity_timing_qualifier 	varchar(20),
	search_confidence_threshold 	integer,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);
create table qri (
	candidate_confidence 			integer,
	match_reason_code 				varchar(2),
	algorithm_descriptor 			varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);


create table rcp (
	query_priority 					integer,
	quantity_limited_request 		varchar(10),
	response_modality 				varchar(250),
	execution_and_delivery_time 	timestamp,
	modify_indicator 				integer,
	sort_by_field 					varchar(512),
	segment_group_inclusion 		varchar(256),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rdf (
	number_of_columns_per_row 		integer,
	column_description 				varchar(40),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rdt (
	column_value 					varchar(999),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rel (
	set_id_rel 								integer primary key,
	relationship_type 						varchar(705),
	this_relationship_instance_identifier 	varchar(60),
	source_information_instance_identifier 	varchar(60),
	target_information_instance_identifier 	varchar(60),
	asserting_entity_instance_id 			varchar(60),
	asserting_person 						varchar(250),
	asserting_organization 					varchar(250),
	assertor_address 						varchar(250),
	assertor_contact 						varchar(250),
	assertion_date_range 					varchar(53),
	negation_indicator 						integer,
	certainty_of_relationship 				varchar(705),
	priority_no 							integer,
	priority_sequence_no_rel_preference_for_consideration 	varchar(250),
	separability_indicator 					integer,


	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rf1 (
	referral_status 				varchar(705),		
	referral_priority 				varchar(705),
	referral_type	 				varchar(705),
	referral_disposition 			varchar(705),
	referral_category 				varchar(705),
	originating_referral_identifier varchar(30),
	effective_date 					timestamp,
	expiration_date 				timestamp,
	process_date 					timestamp,
	referral_reason 				varchar(705),
	external_referral_identifier 	varchar(30),
	referral_documentation_completion_status	varchar(705),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rfi (
	request_date 					timestamp,
	response_due_date 				timestamp,
	patient_consent 				integer,
	date_additional_information_was_submitted 	timestamp,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rgs (
	set_id_rgs 						integer,
	segment_action_code 			integer,
	resource_group_id 				varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rmi (
	risk_management_incident_code 	varchar(250),
	date_time_incident 				timestamp,
	incident_type_code 				varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rol (

	role_instance_id 				varchar(60) primary key,
	action_code 					integer,
	role_rol 						varchar(250),
	role_person 					varchar(250),
	role_begin_date_time 			timestamp,
	role_end_date_time 				timestamp,
	role_duration 					varchar(250),
	role_action_reason 				varchar(250),
	provider_type 					varchar(250),
	organization_unit_type 			varchar(250),
	office_home_address_birthplace	varchar(250),
	phone 							varchar(250),
	persons_location 				varchar(1230),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rq1 (
	anticipated_price 				varchar(10),
	manufacturer_identifier 		varchar(705),
	manufacturer_catalog 			varchar(16),
	vendor_id 						varchar(250),
	vendor_catalog 					varchar(16),
	taxable 						integer,
	substitute_allowed 				integer,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rqd (
	requisition_line_number 		integer,
	item_code_internal				varchar(250),
	item_code_external 				varchar(250),
	hospital_item_code 				varchar(250),
	requisition_quantity 			integer,
	requisition_unit_of_measure 	varchar(250),
	cost_center_account_number 		varchar(30),
	item_natural_account_code 		varchar(30),
	deliver_to_id 					varchar(250),
	date_needed 					timestamp,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rxa (

	give_sub_id_counter 			integer,
	administration_sub_id_counter 	integer,
	date_time_start_of_administration	timestamp,
	date_time_end_of_administration 	timestamp,
	administered_code 				varchar(250),
	administered_amount 			integer,
	administered_units 				varchar(250),
	administered_dosage_form 		varchar(250),
	administration_notes 			varchar(250),
	administering_provider 			varchar(250),
	administered_at_location 		varchar(200),
	administered_per_time_unit 		varchar(20), 	
	administered_strength 			integer,
	administered_strength_units 	varchar(250),
	substance_lot_number 			varchar(20),
	substance_expiration_date 		timestamp,
	substance_manufacturer_name 	varchar(250),
	substance_treatment_refusal_reason	varchar(250),
	indication 						varchar(250),
	completion_status 				integer,
	action_code_rxa 				integer,
	system_entry_date_time 			timestamp,
	administered_drug_strength_volume 	integer,
	administered_drug_strength_volume_units 	varchar(250),
	administered_barcode_identifier	varchar(60),
	pharmacy_order_type 			integer,
	administer_at 					varchar(180),
	administered_at_address 		varchar(106),


	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rxc (
	rx_component_type 				integer,
	component_code 					varchar(250),
	component_amount 				integer,
	component_units 				varchar(250),
	component_strength 				integer,
	component_strength_units 		varchar(250),
	supplementary_code 				varchar(250),
	component_drug_strength_volume 	integer,
	component_drug_strength_volume_units 	varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);


create table rxd (
	dispense_sub_id_counter			integer,
	dispensegive_code				varchar(250),
	datetime_dispensed 				timestamp,
	actual_dispense_amount 			integer,
	actual_dispense_units 			varchar(250),
	actual_dosage_form 				varchar(250),
	prescription_number 			varchar(20),
	number_of_refills_remaining 	integer,
	dispense_notes 					varchar(200),
	dispensing_provider 			varchar(200),
	substitution_status 			integer,
	total_daily_dose 				varchar(10),
	dispense_to_location 			varchar(200),
	needs_human_review 				integer,
	pharmacy_treatment_supplier_special_dispensing_instructions		varchar(250),
	actual_strength 				integer,
	actual_strength_unit 			varchar(250),
	substance_lot_number 			varchar(20),
	substance_expiration_date 		timestamp,
	substance_manufacturer_name 	varchar(250),
	indication 						varchar(250),
	dispense_package_size 			integer,
	dispense_package_size_unit 		varchar(250),
	dispense_package_method			integer, 	
	supplementary_code 				varchar(250),
	initiating_location 			varchar(250),
	packaging_assembly_location 	varchar(250),
	actual_drug_strength_volume 	integer,
	actual_drug_strength_volume_units	 varchar(250),
	dispense_to_pharmacy 			integer,
	dispense_to_pharmacy_address 	varchar(106),
	pharmacy_order_type 			integer,
	dispense_type 					varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rxe (
	quantity_or_timing 				varchar(250),
	give_code 						varchar(250),
	give_amount_minimum 			integer,
	give_amount_maximum 			integer,
	give_units 						varchar(250),
	give_dosage_form 				varchar(250),
	provider_administration_instructions 	varchar(250),
	deliver_to_location 			varchar(250),
	substitution_status 			integer,
	dispense_amount 				integer,
	dispense_units 					varchar(250),
	number_of_refills 				integer,
	ordering_provider_dea_number 	varchar(250),
	pharmacist_treatment_supplier_verifier_id 	varchar(250),
	prescription_number 			varchar(20),
	number_of_refills_remaining		integer,
	number_of_refills_or_doses_dispensed 	integer,
	dt_of_most_recent_refill_or_dose_dispensed	timestamp,
	total_daily_dose 				varchar(10),
	needs_human_review 				integer,
	pharmacy_treatment_supplier_special_dispensing_instructions	varchar(250),
	give_per_time_unit 				varchar(20),
	give_rate_amount 				varchar(6),
	give_rate_units 				varchar(250),
	give_strength 					integer,
	give_strength_units 			varchar(250),
	give_indication 				varchar(250),
	dispense_package_size 			integer,
	dispense_package_size_unit 		varchar(250),
	dispense_package_method 		integer,
	supplementary_code 				varchar(250),
	original_order_date_time 		timestamp,
	give_drug_strength_volume 		integer,
	give_drug_strength_volume_units	varchar(250),
	controlled_substance_schedule 	varchar(60),
	formulary_status				integer,
	pharmaceutical_substance_alternative	varchar(60),
	pharmacy_of_most_recent_fill 	varchar(250),
	initial_dispense_amount 		integer,
	dispensing_pharmacy 			integer,
	dispensing_pharmacy_address 	varchar(250),
	deliver_to_patient_location 	varchar(80),
	deliver_to_address 				varchar(250),
	pharmacy_order_type 			integer,

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rxg (
	give_sub_id_counter 			integer,
	dispense_sub_id_counter			integer,
	quantity_timing 				varchar(120),
	give_code 						varchar(250),
	give_amount_minimum 			integer,
	give_amount_maximum 			integer,
	give_units 						varchar(250),
	give_dosage_form 				varchar(250),
	administration_notes 			varchar(250),
	substitution_status 			integer,
	dispense_to_location 			varchar(250),
	needs_human_review 				integer,
	pharmacy_treatment_suppliers_special_administration_instructions 		varchar(250),
	give_per_time_unit 				varchar(20),
	give_rate_amount 				varchar(6),
	give_rate_units 				varchar(250),
	give_strength 					integer,
	give_strength_units 			varchar(250),
	substance_lot_number 			varchar(20),
	substance_expiration_date 		timestamp,
	substance_manufacturer_name 	varchar(250),
	indication 						varchar(250),
	give_drug_strength_volume 		integer,
	give_drug_strength_volume_units varchar(250),
	give_barcode_identifier 		varchar(60),
	pharmacy_order_type	 			integer,
	dispense_to_pharmacy 			varchar(180),
	dispense_to_pharmacy_address 	varchar(106),
	deliver_to_patient_location 	varchar(80),
	deliver_to_address				varchar(250),

	patient_id              		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rxo (
	requested_give_code 			varchar(250),
	requested_give_amount_minimum 	integer,
	requested_give_amount_maximum 	integer,
	requested_give_units 			varchar(250),
	requested_dosage_form 			varchar(250),
	provider_pharmacy_or_treatment_instructions 	varchar(250),
	providers_administration_instructions 			varchar(250),
	deliverto_location 				varchar(250),
	allow_substitutions 			integer,
	requested_dispense_code 		varchar(250),
	requested_dispense_amount 		integer,
	requested_dispense_units 		varchar(250),
	number_of_refills				integer,
	ordering_provides_dea_number 	varchar(250),
	pharmacist_or_treatment_suppliers_verifier_id 	varchar(250),
	needs_human_review 				integer,
	requested_give_per_time_unit 	varchar(20),
	requested_give_strength 		integer,
	requested_give_strength_units 	varchar(250),
	indication 						varchar(250),
	requested_give_rate_amount 		varchar(6),
	requested_give_rate_units 		varchar(250),
	total_daily_dose 				varchar(10),
	supplementary_code 				varchar(250),
	requested_drug_strength_volume 	integer,
	requested_drug_strength_volume_units 	varchar(250),
	pharmacy_order_type 			integer,
	dispensing_interval 			integer,
	medication_instance_identifier 	varchar(60),
	segment_instance_identifier 	varchar(60),
	mood_code 						varchar(2),
	dispensing_pharmacy 			varchar(250),
	dispensing_pharmacy_address 	varchar(250),
	deliver_to_patient_location 	varchar(80),
	deliver_to_address 				varchar(250),

	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table rxr (
	route 							varchar(250),
	administration_site 			varchar(250),
	administration_device 			varchar(250),
	administration_method 			varchar(250),
	routing_instruction 			varchar(250),
	administration_site_modifier 	varchar(250),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table sac (
	external_accession_identifier	varchar(427),	
	accession_identifier 			varchar(427),
	container_identifier 			varchar(427),
	primary_parent_container_identifier	varchar(427),
	equipment_container_identifier	varchar(427),
	specimen_source 				varchar(50),
	registration_datetime 			timestamp,
	container_status 				varchar(705),
	carrier_type 					varchar(705),
	carrier_identifier 				varchar(705),
	position_in_carrier 			varchar(80),
	tray_type_sac 					varchar(705),
	tray_identifier 				varchar(427),
	position_in_tray 				varchar(80),
	location 						varchar(705),
	container_height 				varchar(20),
	container_diameter 				varchar(20),
	barrier_delta 					varchar(20),
	bottom_delta 					varchar(20),
	container_height_or_diameter_or_delta_units 	varchar(705),
	container_volume 				varchar(20),
	available_specimen_volume 		varchar(20),
	initial_specimen_volume 		varchar(20),
	volume_units 					varchar(705),
	separator_type 					varchar(705),
	cap_type 						varchar(705),
	additive 						varchar(705),
	specimen_component 				varchar(705),
	dilution_factor 				varchar(36),
	treatment 						varchar(705),
	temperature 					varchar(36),
	hemolysis_index 				varchar(20),
	hemolysis_index_units 			varchar(705),
	lipemia_index 					varchar(20),
	lipemia_index_units 			varchar(705),
	icterus_index 					varchar(20),
	icterus_index_units 			varchar(705),
	fibrin_index 					varchar(20),
	fibrin_index_units 				varchar(705),
	system_induced_contaminants 	varchar(705),
	drug_interference 				varchar(705),
	artificial_blood 				varchar(705),
	special_handling_code 			varchar(705),
	other_environmental_factors 	varchar(705),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table scd (
	cycle_start_time 				timestamp,
	cycle_count 					integer,
	temp_max 						varchar(36),
	temp_min						varchar(36),
	load_number						integer,
	condition_time 					varchar(36),
	sterilize_time 					varchar(36),
	exhaust_time 					varchar(16),
	total_cycle_time 				varchar(16),
	device_status 					varchar(4),
	cycle_start_datetime 			timestamp,
	dry_time 						varchar(16),
	leak_rate 						varchar(16),
	control_temperature 			varchar(36),
	sterilizer_temperature 			varchar(36),
	cycle_complete_time 			timestamp,
	under_temperature 				varchar(36),
	over_temperature 				varchar(36),
	abort_cycle 					varchar(4),
	alarm 							varchar(4),
	long_in_charge_phase 			varchar(4),
	long_in_exhaust_phase 			varchar(4),
	long_in_fast_exhaust_phase 		varchar(4),
	reset 							varchar(4),
	operator_unload 				varchar(15),
	door_open 						varchar(4),
	reading_failure 				varchar(4),
	cycle_type 						varchar(3),
	thermal_rinse_time 				varchar(16),
	wash_time 						varchar(16),
	injection_rate 					varchar(16),
	procedure_code 					varchar(705),
	patient_identifier_list 		varchar(250),
	attending_doctor 				varchar(250),
	dilution_factor 				varchar(36),
	fill_time 						varchar(16),
	inlet_temperature 				varchar(36),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table sch (
	placer_appointment_id 			varchar(75),
	filler_appointment_id 			varchar(75),
	occurrence_number 				integer,
	placer_group_number 			varchar(22),
	schedule_id 					varchar(250),
	event_reason 					varchar(250),
	appointment_reason 				varchar(250),
	appointment_type 				varchar(250),
	appointment_duration 			integer,--datatime ? integer?
	appointment_duration_units		varchar(50),
	appointment_timing_quantity 	varchar(250),
	placer_contact_person 			varchar(250),
	placer_contact_phone_number 	varchar(250),
	placer_contact_address 			varchar(250),
	placer_contact_location 		varchar(80),
	filler_contact_person 			varchar(250),
	filler_contact_phone_number 	varchar(250),
	filler_contact_address 			varchar(250),
	filler_contact_location 		varchar(80),
	entered_by_person 				varchar(250),
	entered_by_phone_number 		varchar(250),
	entered_by_location 			varchar(80),
	parent_placer_appointment_id 	varchar(75),
	parent_filler_appointment_id 	varchar(75),
	filler_status_code 				varchar(250),
	placer_order_number 			varchar(427),
	filler_order_number 			varchar(427),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table scp (
	labor_calculation_type 			varchar(250),
	date_format 					varchar(250),
	device_number 					varchar(8),
	device_name 					varchar(999),
	device_model_name 				varchar(2),
	device_type 					varchar(250),
	lot_control 					varchar(250),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table sdd (
	lot_number 						varchar(11),
	device_number 					varchar(8),
	device_name 					varchar(999),
	device_data_state 				integer,
	load_status 					integer,
	control_code 					integer,
	operator_name 					varchar(15),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table sft (
	software_vendor_organization	varchar(567),
	software_certified_version_or_release_number	varchar(15),
	software_product_name			varchar(20),
	software_binary_id				varchar(20),
	software_product_information	varchar(1024),
	software_install_date			timestamp,
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table sid (
	application_identifier 			varchar(705),
	substance_lot_number 			varchar(20),
	substance_container_identifier 	varchar(200),
	substance_manufacturer_identifier	varchar(705),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table slt (
	device_number					varchar(8),
	device_name						varchar(999),
	lot_number						varchar(11),
	item_identifier					varchar(250),
	bar_code						varchar(30),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table spm (
	set_id_spm						integer primary key,
	specimen_id 					varchar(855),			
	specimen_parent_ids				varchar(855),		
	specimen_type 					varchar(705),
	specimen_type_modifier	 		varchar(705),
	specimen_additives 				varchar(705),
	specimen_collection_method		varchar(705),
	specimen_source_site 			varchar(705),
	specimen_source_site_modifier	varchar(705),
	specimen_collection_site 		varchar(705),
	specimen_role 					varchar(705),
	specimen_collection_amount 		varchar(20),
	grouped_specimen_count 			integer,
	specimen_description			varchar(250),
	specimen_handling_code			varchar(705),
	specimen_risk_code				varchar(705),
	specimen_collection_date_time	varchar(49), --time range
	specimen_received_date_time		timestamp,
	specimen_expiration_date_time	timestamp,
	specimen_availability			boolean,
	specimen_reject_reason			varchar(705),
	specimen_quality				varchar(705),
	specimen_appropriateness		varchar(705),
	specimen_condition				varchar(705),
	specimen_current_quantity		varchar(722),
	number_of_specimen_containers	integer,
	container_type					varchar(705),
	container_condition				varchar(705),
	specimen_child_role				varchar(705),
	patient_id               		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table stf (
	primary_key_value_stf			varchar(250),
	staff_identifier_list			varchar(250),
	staff_name						varchar(250),
	staff_type						integer,
	administrative_sex 				integer,
	datetime_of_birth				timestamp,
	activeinactive_flag				boolean,				
	department 						varchar(250),
	hospital_service_stf 			varchar(250),
	phone 							varchar(250),
	officehome_address_birthplace	varchar(250),
	institution_activation_date 	timestamp,
	institution_inactivation_date	timestamp,
	backup_person_id 				integer,
	email_address					varchar(40),
	preferred_method_of_contact 	varchar(705),
	marital_status 					varchar(705),
	job_title						varchar(20),
	job_code_class 					varchar(20),				
	employment_status_code			varchar(250),
	additional_insured_on_auto 		integer,
	drivers_license_number_of_staff	varchar(25),	
	copy_auto_ins					integer,
	auto_ins_expires				timestamp,
	date_last_dmv_review			timestamp,
	date_next_dmv_review			timestamp,
	race 							timestamp,
	ethnic_group					varchar(705),
	reactivation_approval_indicator	integer,	
	citizenship						varchar(705),
	datetime_of_death				timestamp,
	death_indicator					integer,
	institution_relationship_type_code	varchar(250),
	institution_relationship_period		varchar(52),
	expected_return_date				timestamp,
	cost_center_code					varchar(250),
	generic_classification_indicator	integer,
	inactive_reason_code				varchar(250),
	generic_resource_type_or_category	varchar(10),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table stz (
	sterilization_type 				varchar(250),
	sterilization_cycle				varchar(250),
	maintenance_cycle				varchar(250),
	maintenance_type				varchar(250),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table tcc (
	universal_service_identifier	varchar(705),
	equipment_test_application_identifier	varchar(427),
	specimen_source 				varchar(100), --not clear
	auto_dilution_factor_default	varchar(36),
	rerun_dilution_factor_default	varchar(36),
	pre_dilution_factor_default 	varchar(36),
	endogenous_content_of_pre_dilution_diluent	varchar(36),
	inventory_limits_warning_level 	integer,
	automatic_rerun_allowed			integer,
	automatic_repeat_allowed 		integer,
	automatic_reflex_allowed		integer,
	equipment_dynamic_range			varchar(36),
	units 							varchar(705),
	processing_type 				varchar(705),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table tcd (
	universal_service_identifier 	varchar(705),
	auto_dilution_factor 			varchar(36),
	rerun_dilution_factor	   		varchar(36),
	pre_dilution_factor 			varchar(36),
	endogenous_content_of_pre_dilution_diluent	varchar(36),
	automatic_repeat_allowed 		integer,
	reflex_allowed 					integer,
	analyte_repeat_status	 		varchar(705),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table tq1 (	 
	set_id_tq1						integer primary key,
	quantity   						integer,						
	repeat_pattern 					varchar(540),
	explicit_time					timestamp,
	relative_time_and_units 		varchar(20),
	service_duration 				varchar(20),
	start_datetime	 				timestamp,
	end_datetime  					timestamp,
	priority 						varchar(250),
	condition_text					varchar(250), 					
	text_instruction 				varchar(250),
	conjunction						integer,
	occurrence_duration 			varchar(20),
	total_occurrences 				integer,
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table tq2 (	 
	set_id_tq2						integer primary key,
	sequence_or_results_flag		boolean,
	related_placer_number 			integer,
	related_filler_number 			integer,
	related_placer_group_number  	integer,
	sequence_condition_code 		integer,
	cyclic_entry_exit_indicator 	boolean,
	sequence_condition_time_interval	varchar(30),
	cyclic_group_max_number_of_repeats	integer,
	special_service_request_relationship	integer, 
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);


create table txa (
	set_id_txa						integer primary key,
	document_type 					varchar(30),
	document_content_presentation	integer,
	activity_datatime 				timestamp,
	primary_activity_provider 		varchar(250),
	origination_datatime 			timestamp,
	transcription_datatime			timestamp,
	edit_datetime					timestamp,
	originator_name	    			varchar(250),
	assigned_document_authenticator	varchar(250),
	transcriptionist_name 			varchar(250),
	unique_document_number 			integer,
	parent_document_number 			integer,
	placer_order_number 			integer,
	filler_order_number 			integer,
	unique_document_file_name 		varchar(30),
	document_completion_status 	    integer,	
	document_confidentiality_status integer,
	document_availability_status 	integer,
	document_storage_status 		integer,
	document_change_reason 			varchar(30),
	authentication_person_timestamp varchar(250), --the data type seems to be time stamp but the length is 250
	distributed_copies 				varchar(250),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table uac (
	User_authentication_credential_type_code	varchar(705),
	User_authentication_credential 	long varchar(65536),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table ub1 (	
	set_id_ub1						integer primary key,
	-- the following  line is not defined in the Excel doc
	blood_deductible				varchar(20),			
	blood_furnished_pints			integer,
	blood_replaced_pints 			integer,
	blood_not_replaced_pints 		integer,
	co_insurance_days 				integer,
	condition_code 					varchar(20),
	covered_days 					integer,
	non_covered_days 				integer,
	value_amount_code 				varchar(250),
	number_of_grace_days 			integer,
	special_program_indicator 		varchar(250),
	PSRO_UR_approval_indicator		varchar(250),
	PSRO_UR_approved_stay_fm 		timestamp,
	PSRO_UR_approved_stay_to 		timestamp,
	occurrence 						varchar(250),
	occurrence_span 				varchar(250),
	occur_span_start_date 			timestamp,
	occur_span_end_date 			timestamp,
	UB_82_locator2 					varchar(30),
	UB_82_locator9 					varchar(30),
	UB_82_locator27 				varchar(30),
	UB_82_locator45 				varchar(30),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);
create table ub2 (
	set_id_ub2						integer primary key,
	co_insurance_days				varchar(3),
	condition_code					varchar(2),
	covered_days 					varchar(3),
	non_covered_days 				varchar(4),
	value_amount_code 				varchar(41),
	occurrence_code_date 			varchar(259),
	occurrence_span_code_dates 		varchar(268),
	UB92_locator2_state 			varchar(30),
	UB92_locator11_state 			varchar(30),
	UB92_locator31_national 		varchar(30),
	document_control_number 		varchar(23),
	UB92_locator49_national 		varchar(30),
	UB92_locator56_state 			varchar(30),
	UB92_locator57_national 		varchar(30),
	UB92_locator78_state 			varchar(30),
	special_visit_count 			integer,
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table urd (
	RU_datetime 					timestamp,
	report_priority					integer,
	RU_who_subject_definition		varchar(250),
	RU_what_subject_definition		varchar(250),
	RU_what_department_code			varchar(250),
	RU_display_print_locations		varchar(20),
	RU_results_level				integer,
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table urs (
	RU_where_subject_definition		varchar(20),
	RU_when_data_start				timestamp,
	RU_when_data_end				timestamp,
	RU_what_user_qualifier			varchar(20),
	RU_other_results_subject_definition	varchar(20),
	RU_which_datetime_qualifier		integer,
	RU_which_datetime_status_qualifier	integer,
	RU_datetime_selection_qualifier	integer,
	-- not sure for the following line
	RU_quantity_timing_qualifier	varchar(100),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table var (
	variance_instance_id			varchar(60) primary key,
	documented_date_time			timestamp,
	stated_variance_date_time 		timestamp,
	variance_originator				varchar(250),
	variance_classification			varchar(705),
	variance_description			varchar(512),
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);

create table vnd (
	set_id							integer primary key,
	vendor_identifier				varchar(250),
	vendor_name						varchar(999),
	vendor_catalog_number			varchar(20),
	-- not sure for the follwwing line!!
	primary_vendor_indicator		boolean,
	-- end 
	patient_id                		integer,
	foreign key (patient_id) references pid (patient_id)
);
