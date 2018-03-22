from vnc_api import vnc_api
vnc_lib = vnc_api.VncApi(api_server_host='10.10.7.149')
vn_blue_obj = vnc_api.VirtualNetwork('vn-blue')
vn_blue_obj.add_network_ipam(vnc_api.NetworkIpam(),vnc_api.VnSubnetsType([vnc_api.IpamSubnetType(subnet = vnc_api.SubnetType('10.0.2.0', 24))]))
vnc_lib.virtual_network_create(vn_blue_obj)

vn_red_obj = vnc_api.VirtualNetwork('vn-red')
vn_red_obj.add_network_ipam(vnc_api.NetworkIpam(),vnc_api.VnSubnetsType([vnc_api.IpamSubnetType(subnet = vnc_api.SubnetType('10.0.3.0', 24))]))
vnc_lib.virtual_network_create(vn_red_obj)
policy_obj = vnc_api.NetworkPolicy('policy-red-blue',network_policy_entries = vnc_api.PolicyEntriesType([vnc_api.PolicyRuleType(direction='<>',action_list = vnc_api.ActionListType(simple_action='pass'), protocol = 'tcp',src_addresses = [vnc_api.AddressType(virtual_network = vn_blue_obj.get_fq_name_str())], src_ports = [vnc_api.PortType(-1, -1)],dst_addresses = [vnc_api.AddressType(virtual_network = vn_red_obj.get_fq_name_str())], dst_ports = [vnc_api.PortType(80, 80)])]))
vnc_lib.network_policy_create(policy_obj)

vn_blue_obj.add_network_policy(policy_obj, vnc_api.VirtualNetworkPolicyType(sequence=vnc_api.SequenceType(0, 0)))
vn_red_obj.add_network_policy(policy_obj, vnc_api.VirtualNetworkPolicyType(sequence=vnc_api.SequenceType(0, 0)))

vnc_lib.virtual_network_update(vn_blue_obj)
vnc_lib.virtual_network_update(vn_red_obj)

print vnc_lib.virtual_network_read(id = vn_blue_obj.uuid)


print vnc_lib.virtual_networks_list()


